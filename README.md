English | [繁體中文](https://github.com/cycleapple/StoryGenerator/blob/main/README_zh.md)

# Short Story Generator

This is a simple Flask app that generates short stories based on a user-provided theme. The app uses the OpenAI GPT-3 API to generate the stories, and allows the user to choose between English and Traditional Chinese language options.

## Installation

To run the app locally, you will need to install Python 3 and the required dependencies by running the command:

pip install -r requirements.txt

You will also need to create a `.env` file in the root directory of the project and add your OpenAI API key to it in the following format:

````
OPENAI_API_KEY=<your-api-key>
````

Replace `<your-api-key>` with your actual API key, which you can obtain from the OpenAI website.

Once you have installed the dependencies and added your API key, you can run the app by running the command:

````
python app.py
````

Then, navigate to `http://localhost:5000` in your web browser to access the app.

## Usage

To use the app, simply enter a theme in the input field and select a language option (English or Traditional Chinese). Then, click the "Generate" button to generate a short story based on the theme.

The app will display a loading animation while it waits for the story to be generated. Once the story is generated, it will be displayed in the main content area of the page.

## Credits

This app was created by [your-name-here]. It uses the [OpenAI GPT-3 API](https://openai.com/api/) for story generation, and was built using [Flask](https://flask.palletsprojects.com/en/2.1.x/) and [Bootstrap](https://getbootstrap.com/).

## License

This app is licensed under the [MIT License](LICENSE). You are free to use and modify it for any purpose, as long as you include attribution to the original author and include a copy of the license file.
