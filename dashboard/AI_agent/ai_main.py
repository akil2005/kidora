from .prompt_templates import generate_image_prompt, generate_story_prompt
#from .image_generator import generate_image

from .generate_story import generate_story 
from .extract_story_data import extract_story_data, extract_story_steps, extract_visual_descriptions
from .post_image_generation.add_text_layer import add_text_to_image

def main_generate(question: str, img_path: str) -> str:
    # Step 3: Generate images using each visual description
    max_tries = 3
    i = 0 
    while i < max_tries:from .prompt_templates import generate_image_prompt, generate_story_prompt
from .image_generator import generate_image  # ✅ must be imported

from .generate_story import generate_story
from .extract_story_data import (
    extract_story_data,
    extract_story_steps,
    extract_visual_descriptions,
)
from .post_image_generation.add_text_layer import add_text_to_image


def main_generate(question: str, img_path: str):
    """
    Main pipeline:
    1. Generate story
    2. Extract structured story data
    3. Generate images
    4. Add text overlays
    """

    max_tries = 3
    story_response = None

    # Try generating a valid 5-step story
    for _ in range(max_tries):
        raw_story = generate_story(question)
        print("Story generated successfully!")

        story_response = extract_story_data(raw_story)
        story_steps = story_response.get("story_steps", [])

        if len(story_steps) == 5:
            break

    if not story_response or len(story_steps) != 5:
        raise ValueError("Failed to generate a valid 5-step story")

    # Generate images for each step
    for i in range(5):
        image_prompt = generate_image_prompt(
            setting=story_response["story_setting"],
            style=story_response["story_style"],
            character=story_response["main_character"],
            visual_scene_description=story_steps[i]["visual_scene_description"],
        )

        print(f"Generating image {i + 1}")

        generated_img_path = generate_image(
            prompt=image_prompt,
            step=i + 1,
            output_dir=img_path,
        )

        add_text_to_image(
            generated_img_path,
            story_steps[i]["story_point"],
        )


# Optional: standalone test (NOT used by Django)
if __name__ == "__main__":
    question = "A detective duck wearing a detective suit is solving the mystery of a missing egg"
    img_path = "./generated_images"

    main_generate(question, img_path)

        raw_story = generate_story(question)
        print("Story generated successfully!")
        # Step 2: Extract structured information from the story
        story_response = extract_story_data(raw_story)
        story_steps = story_response["story_steps"]
        if len(story_steps) == 5:
            break
        i += 1
        
    for i in range(5):
        image_prompt = generate_image_prompt(
            setting=story_response['story_setting'],
            style=story_response['story_style'],
            character=story_response['main_character'],
            visual_scene_description=story_steps[i]["visual_scene_description"],
        )
        print(i+1)
        generated_img_path = generate_image(image_prompt,i+1,img_path)
        add_text_to_image(generated_img_path, story_steps[i]["story_point"])

if __name__ == "__main__":
    # Step 1: Generate the story from question
    question = "A detective duck wearing a detective suit is solving a mystery of an egg"
    raw_story = generate_story(question)
    print("Story generated successfully!")
    # Step 2: Extract structured information from the story
    story_response = extract_story_data(raw_story)
    story_steps = story_response["story_steps"]
    # Step 3: Generate images using each visual description
    for i in range(5):
        image_prompt = generate_image_prompt(
            setting=story_response['story_setting'],
            style=story_response['story_style'],
            character=story_response['main_character'],
            visual_scene_description=story_steps[i]["visual_scene_description"],
        )
        print(i+1)
        generated_img_path = generate_image(image_prompt,i+1)
        add_text_to_image(generated_img_path, story_steps[i]["story_point"])

