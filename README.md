
# YouTube_Summarizer

## Overview

YouTube Summarizer is an application that utilizes Google's Gemini API to generate summaries of YouTube videos. This tool is designed to help users quickly understand the content of videos without having to watch them in their entirety.

## Features

* Summarize YouTube videos using advanced natural language processing.
* Quick and easy-to-understand summaries.
* User-friendly interface.

## Prerequisites
* Python 3.10 installed on your system.
* Google Gemini API

## Installation

1. Clone the repository:

```git clone https://github.com/theAbMan/Youtube_Summarizer.git```

2. Navigate to the project directory:

``` cd Youtube_Summarizer ```

3. Install the required dependencies:

``` pip install -r requirements.txt ```

4. Set up environment variables. Create a ```.env``` file in the project root directory and add the following:
``` GOOGLE_API_KEY = enter_your_gemini/google_api_key```

## Usage

1. Run the application:
``` streamlit run app.py```

2. Enter the Youtube Vide Link in the input section and click ```GET SUMMARY```

3. Demo:
![Youtube_Summarizer gif](/images/summarizer.gif)

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request.

## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md)

