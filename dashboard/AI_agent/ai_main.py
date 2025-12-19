from .prompt_templates import generate_image_prompt
from .image_generator import generate_image
from .post_image_generation.add_text_layer import add_text_to_image


def main_generate(question: str, img_path: str):
    """
    DEMO-STABLE PIPELINE (NO LLM / NO REGEX)
    """

    print("Starting demo story pipeline...")

    story_setting = "A colorful park in the morning"
    story_style = "Cartoon illustration for kids"
    main_character = "A detective duck wearing a coat and hat"

    story_steps = [
        {
            "story_point": "The detective duck arrives at the park.",
            "visual_scene_description": "A yellow duck in detective clothes standing in a green park."
        },
        {
            "story_point": "He finds clues near a picnic basket.",
            "visual_scene_description": "Duck inspecting a picnic basket with a magnifying glass."
        },
        {
            "story_point": "He asks animals for help.",
            "visual_scene_description": "Duck talking to squirrels and birds."
        },
        {
            "story_point": "He finds a hidden nest.",
            "visual_scene_description": "Duck discovering a nest behind bushes."
        },
        {
            "story_point": "The egg is returned safely.",
            "visual_scene_description": "Happy duck returning the egg to the nest."
        },
    ]

    print("Generating images...")

    for i in range(5):
        image_prompt = generate_image_prompt(
            setting=story_setting,
            style=story_style,
            character=main_character,
            visual_scene_description=story_steps[i]["visual_scene_description"],
        )

        print(f"Generating image {i + 1}...")

        generated_img_path = generate_image(
            prompt=image_prompt,
            index=i + 1,
            output_dir=img_path,
        )

        add_text_to_image(
            generated_img_path,
            story_steps[i]["story_point"],
        )

    print("Demo completed successfully!")


# Optional standalone test
if __name__ == "__main__":
    main_generate(
        "A detective duck solving a mystery",
        "./generated_images"
    )
