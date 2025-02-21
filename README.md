<p align="center">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100">
  <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="100">
</p>
<h1 align="center">README-AI</h1>
<p align="center">
    <em>Auto-generate detailed and structured README files, powered by AI.</em>
</p>
<p align="center">
  <a href="https://github.com/eli64s/readme-ai/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/eli64s/readme-ai/.github%2Fworkflows%2Frelease-pipeline.yml?logo=GitHub&label=cicd&color=c125ff" alt="Test">
  </a>
  <a href="https://app.codecov.io/gh/eli64s/readme-ai">
    <img src="https://img.shields.io/codecov/c/github/eli64s/readme-ai?logo=codecov&color=c125ff" alt="Publish">
  </a>
  <a href="https://pypi.python.org/pypi/readmeai/">
    <img src="https://img.shields.io/pypi/v/readmeai?color=c125ff" alt="PyPI Version">
    <img src="https://img.shields.io/pypi/pyversions/readmeai.svg?color=c125ff" alt="Python Versions">
  </a>
</p>

---

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [🤖 Demo](#-demo)
> - [🔮 Features](#-features)
> - [🚀 Getting Started](#-getting-started)
  > - [⚙️ Installation](#️-installation)
  > - [👩‍💻 Running readme-ai](#-running-readme-ai)
  > - [🧩 Configuration](#-configuration)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)

---

## 📍 Overview

***Objective***

Readme-ai is a developer tool that auto-generates README.md files using a combination of data extraction and generative ai. Simply provide a repository URL or local path to your codebase and a well-structured and detailed README file will be generated for you.

***Motivation***

Streamlines documentation creation and maintenance, enhancing developer productivity. This project aims to enable all skill levels, across all domains, to better understand, use, and contribute to open-source software.<br>

> [!IMPORTANT]
>
> This project is currently under development with an opinionated configuration and setup. It is vital to review all text generated by the LLM APIs to ensure it accurately represents your project.

---

## 🤖 Demo

Standard CLI usage with an OpenAI API key (recommended).

[readmeai-cli-demo](https://github.com/eli64s/readme-ai/assets/43382407/ff5b3db8-a400-4031-86fc-a28f8a0469e2)

You can also generate README files without an API key by using the `--offline` CLI option.

[readmeai-cli-offline-demo](https://github.com/eli64s/readme-ai/assets/43382407/a508ab17-6fcf-4de5-9239-fc4055d11d62)

> [!TIP]
>
> Offline mode is useful for quickly generating a boilerplate README without incurring API costs. See an offline mode README file [here](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-offline.md).

<!--
**Streamlit Web App**: Run <em>readme-ai</em> directly in your browser with Streamlit, no installation required!

[readmeai-streamlit-demo](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-offline.md)
-->

---

## 🔮 Features

Built with flexibility in mind, readme-ai allows users to customize various aspects of the README file using CLI options and configuration settings. Content is generated using a combination of data extraction and making a few calls to LLM APIs.

Currently, readme-ai uses generative ai to create four distinct sections of the README file.

> i. **Header**: Project slogan that describes the repository in an engaging way.
>
> ii. **Overview**: Provides an intro to the project's core use-case and value proposition.
>
> iii. **Features**: Markdown table containing details about the project's technical components.
>
> iv. **Modules**: Codebase file summaries are generated and formatted into markdown tables.

All other content is extracted from processing and analyzing repository metadata and files.

### Customizable Header

The header section is built using repository metadata and CLI options. Key features include:
- **Badges**: Svg icons that represent codebase metadata, provided by [shields.io](https://shields.io/) and [skill-icons](https://github.com/tandpfun/skill-icons).
- **Project Logo**: Select a project logo image from the base set or provide your image.
- **Project Slogan**: Catch phrase that describes the project, generated by generative ai.
- **Table of Contents/Quick Links**: Links to the different sections of the README file.

Below are a few examples of README headers generated by the readme-ai tool.
<table>
  <tr>
    <td colspan="2" align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-default.png" alt="large-repo" width="800"/><br>
      <code>default output (no options provided to cli)</code>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-flat.png" alt="flat" width="400"/><br>
      <code>--badges flat --image black</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-offline.png" alt="flat" width="400"/><br>
      <code>--badges flat-square --offline</code>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-plastic.png" alt="plastic" width="400"/><br>
      <code>--badges plastic --image grey</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-purple.png" alt="large-repo" width="400"/><br>
      <code>--align left --badges flat --image purple</code>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-skills-light.png" alt="skills-light" width="400"/><br>
      <code>--badges skills-light --image grey</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-skills-dark.png" alt="skills" width="400"/><br>
      <code>--align left --badges skills --image yellow</code>
    </td>
  </tr>
</table>

See the <a href="#-configuration">Configuration</a> section below for the complete list of CLI options and settings.<br>
<!-- -->
<details closed>
  <summary>📑 Codebase Documentation</summary>
  <br>
  <table>
    <tr>
      <td>
        <b>Repository Structure</b><br>
        <p>A directory tree structure is created and displayed in the README. Implemented using pure Python (<a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tree.py">tree.py</a>).</p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/code-directory-tree.png" alt="tree" width="700" />
      </td>
    </tr>
    <tr>
      <td style="padding-top:20px;">
        <b>Codebase Summaries</b>
        <br>
        <p>File summaries generated using LLM APIs, and are formatted and grouped by directory in markdown tables.</p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/code-summary-table.png" alt="summaries" width="700" />
      </td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>📍 Overview & Features Table</summary>
  <br>
  The overview and features sections are generated using OpenAI's API. Structured prompt templates are injected with repository metadata to help produce more accurate and relevant content.
  <br>
  <table>
    <tr>
      <td><b>Overview</b><br>
        <p>High-level introduction of the project, focused on the value proposition and use-cases, rather than technical aspects.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/overview.png" alt="overview" width="700" /></td>
    </tr>
    <tr>
      <td style="padding-top:20px;"><b>Features Table</b><br>
        <p>Describes technical components of the codebase, including architecture, dependencies, testing, integrations, and more.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/features-table.png" alt="features-table" width="700" /></td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>🚀 Dynamic Quick Start Guides</summary>
  <br>
  <table>
    <tr>
      <td><b>Getting Started or Quick Start</b><br>
        <p>Generates structured guides for installing, running, and testing your project. These steps are created by identifying dependencies and languages used in the codebase, and mapping this data to configuration files such as the <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_setup.toml">language_setup.toml</a> file.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/getting-started.png" alt="getting-started" width="700" />
      </td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>🤝 Contributing Guidelines, License, & More</summary>
  <br>
  <table>
    <tr>
      <td><b>Additional Sections</b><br>
        <p>The remaining README sections are built from a baseline template that includes common sections such as <code>Project Roadmap, Contributing Guidelines, License, and Acknowledgements</code>.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/contributing.png" alt="contributing-guidelines" width="700" /></td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>🧩 Templates</summary>
  <br>This feature is currently under development. The template system will allow users to generate README files in different flavors, such as ai, data, web development, etc.
  <br>
  <table>
    <tr>
      <td>
        <h3>README Template for ML & Data</h3>
        <ul>
          <li><a href="#overview">Overview</a>: Project objectives, scope, outcomes.</li>
          <li><a href="#project-structure">Project Structure</a>: Organization and components.</li>
          <li><a href="#data-preprocessing">Data Preprocessing</a>: Data sources and methods.</li>
          <li><a href="#feature-engineering">Feature Engineering</a>: Impact on model performance.</li>
          <li><a href="#model-architecture">Model Architecture</a>: Selection and development strategies.</li>
          <li><a href="#training-and-validation">Training</a>: Procedures, tuning, strategies.</li>
          <li><a href="#testing-and-evaluation">Testing and Evaluation</a>: Results, analysis, benchmarks.</li>
          <li><a href="#deployment">Deployment</a>: System integration, APIs.</li>
          <li><a href="#usage">Usage and Maintenance</a>: User guide, model upkeep.</li>
          <li><a href="#results">Results and Discussion</a>: Implications, future work.</li>
          <li><a href="#ethical-considerations">Ethical Considerations</a>: Ethics, privacy, fairness.</li>
          <li><a href="#contributing">Contributing</a>: Contribution guidelines.</li>
          <li><a href="#acknowledgements">Acknowledgements</a>: Credits, resources used.</li>
          <li><a href="#license">License</a>: Usage rights, restrictions.</li>
        </ul>
      </td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>🎨 Examples</summary>
  <br>
  <table>
    <thead>
      <tr>
        <th></th>
        <th>Output File</th>
        <th>Repository</th>
        <th>Languages</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-python.md">readme-python.md</a></td>
        <td><a href="https://github.com/eli64s/readme-ai">readme-ai</a></td>
        <td>Python</td>
      </tr>
      <tr>
        <td>2️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-typescript.md">readme-typescript.md</a></td>
        <td><a href="https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript">chatgpt-app-react-typescript</a></td>
        <td>TypeScript, React</td>
      </tr>
      <tr>
        <td>3️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-javascript.md">readme-javascript.md</a></td>
        <td><a href="https://github.com/idosal/assistant-chat-gpt-javascript">(repository deleted)</a></td>
        <td>JavaScript, React</td>
      </tr>
      <tr>
        <td>4️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-kotlin.md">readme-kotlin.md</a></td>
        <td><a href="https://github.com/rumaan/file.io-Android-Client">file.io-android-client</a></td>
        <td>Kotlin, Java, Android</td>
      </tr>
      <tr>
        <td>5️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-rust-c.md">readme-rust-c.md</a></td>
        <td><a href="https://github.com/DownWithUp/CallMon">rust-c-app</a></td>
        <td>C, Rust</td>
      </tr>
      <tr>
        <td>6️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-go.md">readme-go.md</a></td>
        <td><a href="https://github.com/olliefr/docker-gs-ping">go-docker-app</a></td>
        <td>Go</td>
      </tr>
      <tr>
        <td>7️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-java.md">readme-java.md</a></td>
        <td><a href="https://github.com/avjinder/Minimal-Todo">java-minimal-todo</a></td>
        <td>Java</td>
      </tr>
      <tr>
        <td>8️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-fastapi-redis.md">readme-fastapi-redis.md</a></td>
        <td><a href="https://github.com/FerrariDG/async-ml-inference">async-ml-inference</a></td>
        <td>Python, FastAPI, Redis</td>
      </tr>
      <tr>
        <td>9️⃣</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-mlops.md">readme-mlops.md</a></td>
        <td><a href="https://github.com/GokuMohandas/mlops-course">mlops-course</a></td>
        <td>Python, Jupyter</td>
      </tr>
      <tr>
        <td>🔟</td>
        <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-pyflink.md">readme-pyflink.md</a></td>
        <td><a href="https://github.com/eli64s/flink-flow">flink-flow</a></td>
        <td>PyFlink</td>
      </tr>
    </tbody>
  </table>
</details>

---

## 🚀 Getting Started

**Requirements**

* Python: 3.9+
* Package manager or container runtime: `pip` or `docker` recommended.
* OpenAI API account and API key (other providers coming soon)

**Repository**

A repository URL or local path to your codebase is required run readme-ai. The following are supported:
* [GitHub](https://github.com/)
* [GitLab](https://gitlab.com/)
* [Bitbucket](https://bitbucket.org/)
* [File System](https://en.wikipedia.org/wiki/File_system)

**OpenAI API Key**

An OpenAI API account and API key are needed to use *readme-ai*. The following steps outline the process.

<details closed>
  <summary>🔐 OpenAI API Account Setup</summary>
  <ol>
    <li>Go to the <a href="https://platform.openai.com/">OpenAI website</a>.</li>
    <li>Click the "Sign up for free" button.</li>
    <li>Fill out the registration form with your information and agree to the terms of service.</li>
    <li>Once logged in, click on the "API" tab.</li>
    <li>Follow the instructions to create a new API key.</li>
    <li>Copy the API key and keep it in a secure place.</li>
  </ol>
</details>

> [!WARNING]
>
> Before using readme-ai, its essential to understand the potential risks and costs associated with using AI-powered tools.
>
> * **Review Sensitive Information**: Ensure all content in your repository is free of sensitive information before running the tool. This project does not remove sensitive data from your codebase, nor from the output README file.
>
> * **API Usage Costs**: The OpenAI API is not free and costs can accumulate quickly! You will be charged for each request made by readme-ai. Be sure to monitor API usage costs using the [OpenAI API Usage Dashboard](https://platform.openai.com/account/usage).

---

### ⚙️ Installation

Using `pip`
```sh
pip install readmeai
```

Using `docker`
```sh
docker pull zeroxeli/readme-ai:latest
```

Using `conda`
```sh
conda install -c conda-forge readmeai
```

Alternatively, clone the readme-ai repository and build from source.

```sh
git clone https://github.com/eli64s/readme-ai && \
cd readme-ai
```

Then use one of the methods below to install the project's dependencies (Bash, Conda, Pipenv, or Poetry).

Using `bash`
```sh
bash setup/setup.sh
```

Using `pipenv`
```sh
pipenv install && \
pipenv shell
```

Using `poetry`
```sh
poetry install && \
poetry shell
```

---

### 👩‍💻 Running *README-AI*

Before running the application, ensure you have an OpenAI API key and its set as an environment variable.

On `Linux` or `MacOS`
```console
$ export OPENAI_API_KEY=YOUR_API_KEY
```

On `Windows`
```console
$ set OPENAI_API_KEY=YOUR_API_KEY
```

Use one of the methods below to run the application (Pip, Docker, Conda, Streamlit, etc).

Using `pip`
```sh
readmeai --repository https://github.com/eli64s/readme-ai
```

Using `docker`

```sh
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
-r https://github.com/eli64s/readme-ai
```

Using `conda`
```sh
readmeai -r https://github.com/eli64s/readme-ai
```

Using `streamlit`

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://readmeai.streamlit.app/)

> [!NOTE]
>
> The web app is hosted on <a href="https://streamlit.io/">Streamlit Community Cloud</a>, a free service for sharing Streamlit apps. Thus, the app may be unstable or unavailable at times. See the <a href="https://github.com/eli64s/readme-ai-streamlit">readme-ai-streamlit</a> repository for more details.

<details closed><summary>Alternatively, run the application locally from the cloned repository.</summary><br>

Using `pipenv`
```sh
pipenv shell && \
python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

Using `poetry`
```sh
poetry shell && \
poetry run python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

</details>

---

### 🧪 Tests

Use [`pytest`](https://docs.pytest.org/en/7.1.x/contents.html) to run the default test suite.
```sh
make test
```

Use [`nox`](https://nox.thea.codes/en/stable/) to run the test suite against multiple Python versions including `(3.9, 3.10, 3.11, 3.12)`.
```sh
nox -f noxfile.py
```

---

### 🧩 Configuration

Run the `readmeai` command in your terminal with the following options to tailor your README file.

#### Command-Line Options

| Flag (Long/Short) | Default | Description | Type | Status |
|-------------------|---------|-------------|------|--------|
| `--align`/`-a` | `center` | Set header text alignment (`left`, `center`). | String | Optional |
| `--api-key`/`-k` | `OPENAI_API_KEY` env var | Your GPT model API key. | String | Optional |
| `--badges`/`-b` | `default` | Badge style options for your README file. | String | Optional |
| `--emojis`/`-e` | `False` | Add emojis to section header tiles. | Boolean | Optional |
| `--image`/`-i` | `default` | Project logo image displayed in README header. | String | Optional |
| `--max-tokens` | `3899` | Max number of tokens that can be generated. | Integer | Optional |
| `--model`/`-m` | `gpt-3.5-turbo` | Select GPT model for content generation. | String | Optional |
| `--offline` | `False` | Generate a README without an API key. | Boolean | Optional |
| `--output`/`-o` | `readme-ai.md` | README output file name. | Path/String | Optional |
| `--repository`/`-r` | None | Repository URL or local path. | URL/String | Required |
| `--temperature`/`-t` | `0.8` | LLM API creativity level. | Float | Optional |
| `--template` | None | Choose README template. | String | <em>WIP</em> |
| `--language`/`-l` | `English (en)` | Language for content. | String | <em>WIP</em> |

<sub><em>WIP</em> = work in progress, or feature currently under development.<br>For additional command-line information, run <code>readmeai --help</code> in your terminal for more details about each option.</sub><br>

**Badge Icons**

Select your preferred badge icon style to display in your output file using the `--badges` flag. The default badge style displays basic metadata about your repository using shields.io badges. If you select another option, the `default` badges will be automatically included.

| **Options**      | **Preview** |
|------------------|----------|
| `default`        | ![license](https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff) ![last-commit](https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff) ![languages](https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff) ![language-count](https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff) |
| `flat`           | ![flat](https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white) |
| `flat-square`    | ![flat-square](https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white) |
| `for-the-badge`  | ![for-the-badge](https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white) |
| `plastic`        | ![plastic](https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white) |
| `skills`          | [![Skills](https://skillicons.dev/icons?i=py)](https://skillicons.dev) |
| `skills-light`    | [![Skills-Light](https://skillicons.dev/icons?i=py&theme=light)](https://skillicons.dev) |
| `social`         | ![social](https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=white) |

<br>

**Project Logo**

Select an image to display in your README header section using the `--image` flag.

| **Image**    | Default | Black | Grey | Purple | Yellow |
|--------------|-------|------|------|--------|--------|
| **Preview**  | <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" height="100" id="markdown"> | <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100" height="100" id="markdown"> | <img width="96" height="96" src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" alt="external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo"/> | <img width="100" height="100" src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" alt="external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo"/> | <img src="https://img.icons8.com/pulsar-color/96/markdown.png" width="100" height="100" id="markdown"> |

To provide your own image, use the CLI option `--image custom` and you will be prompted to enter a URL to your image.
<br>

#### Custom Settings

The readme-ai tool is designed with flexibility in mind, allowing users to configure various aspects of its operation through a series of models and settings. The [configuration file](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml) covers aspects such as language model settings, git host providers, repository details, markdown templates, and more.

<details closed><summary>🔠 Configuration Models</summary>
<br>

<!--
# README-AI Configuration and Settings
This documentation provides an overview of the configuration and settings for the README.ai CLI tool. It details various data models and functions that are used to configure the tool, making it adaptable for different environments and use cases.
-->

***GitService Enum***

- **Purpose**: Defines Git service details.
- **Attributes**:
  - `LOCAL`, `GITHUB`, `GITLAB`, `BITBUCKET`: Enumerations for different Git services.
  - `host`: Service host URL.
  - `api_url`: API base URL for the service.
  - `file_url`: URL format for accessing files in the repository.

***BadgeOptions Enum***

- **Purpose**: Provides options for README file badge icons.
- **Options**: `FLAT`, `FLAT_SQUARE`, `FOR_THE_BADGE`, `PLASTIC`, `SKILLS`, `SKILLS_LIGHT`, `SOCIAL`.

***ImageOptions Enum***

- **Purpose**: Lists CLI options for README file header images.
- **Options**: `CUSTOM`, `BLACK`, `BLUE`, `GRADIENT`, `PURPLE`, `YELLOW`.

***CliSettings***

- **Purpose**: Defines CLI options for the application.
- **Fields**:
  - `emojis`: Enables or disables emoji usage.
  - `offline`: Indicates offline mode operation.

***FileSettings***

- **Purpose**: Configuration for various file paths used in the application.
- **Fields**: `dependency_files`, `identifiers`, `ignore_files`, `language_names`, `language_setup`, `output`, `shields_icons`, `skill_icons`.

***GitSettings***

- **Purpose**: Manages repository settings and validations.
- **Fields**:
  - `repository`: The repository URL or path.
  - `source`: The source of the Git repository.
  - `name`: The name of the repository.

***LlmApiSettings***

- **Purpose**: Holds settings for OpenAI's LLM API.
- **Fields**: `content`, `endpoint`, `encoding`, `model`, `rate_limit`, `temperature`, `tokens`, `tokens_max`.

***MarkdownSettings***

- **Purpose**: Contains Markdown templates for different sections of a README.
- **Fields**: Templates for aligning text, badges, headers, images, features, getting started, overview, tables of contents, etc.

***PromptSettings***

- **Purpose**: Configures prompts for OpenAI's LLM API.
- **Fields**: `features`, `overview`, `slogan`, `summaries`.

***AppConfig***

- **Purpose**: Nested model encapsulating all application configurations.
- **Fields**: `cli`, `files`, `git`, `llm`, `md`, `prompts`.

***AppConfigModel***

- **Purpose**: Pydantic model for the entire application configuration.
- **Sub-models**: `AppConfig`.

***ConfigHelper***

- **Purpose**: Assists in loading additional configuration files.
- **Methods**: `load_helper_files` to load configuration from different files.

***Functions***

***`_get_config_dict`***

- **Purpose**: Retrieves configuration data from TOML files.
- **Parameters**:
  - `handler`: Instance of `FileHandler`.
  - `file_path`: Path to the configuration file.

***`load_config`***

- **Purpose**: Loads the main configuration file.
- **Parameters**:
  - `path`: Path to the configuration file.
- **Returns**: An instance of `AppConfig`.

***`load_config_helper`***

- **Purpose**: Loads multiple configuration helper files.
- **Parameters**:
  - `conf`: An instance of `AppConfigModel`.
- **Returns**: An instance of `ConfigHelper`.

***Usage***

The configurations are loaded using the `load_config` function, which parses a TOML file into the `AppConfigModel`. This model is then used throughout the application to access various settings. Additional helper files can be loaded using `ConfigHelper`, which further enriches the application's configuration context.

</details>

<p align="right">
  <a href="#top"><b>Return</b></a>
</p>

---

## 🛠 Project Roadmap

- [X] Publish readme-ai CLI as a Python package on PyPI.
  - [*PyPI Package*](https://pypi.org/project/readmeai/)
- [X] Containerize the readme-ai CLI as a Docker image via Docker Hub.
  - [*Docker Hub Image*](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general)
- [X] Serve the readme-ai CLI as a web app, deployed on Streamlit Community Cloud.
  - [*Streamlit Web Application*](https://readmeai.streamlit.app/)
- [ ] Integrate singular interface for all LLM API providers (Anthropic, Cohere, Gemini, etc.)
- [ ] Design template system to give users a variety of README document flavors (ai, data, web, etc.)
- [ ] Develop robust documentation generation process to extend to full project docs (i.e. Sphinx, MkDocs, etc.)
- [ ] Add support for generating README files in any language (i.e. CN, ES, FR, JA, KO, RU).
- [ ] Create GitHub Actions script to automatically update README file content on repository push.

---

## 📒 Changelog

[Changelog](https://github.com/eli64s/readme-ai/blob/main/CHANGELOG.md)

---

## 🤝 Contributing

- [Discussions](https://github.com/eli64s/readme-ai/discussions)
- [Open an Issue](https://github.com/eli64s/readme-ai/issues)
- [Contributing Guidelines](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)

---

## 📄 License

[MIT](https://github.com/eli64s/readme-ai/blob/main/LICENSE)

---

## 👏 Acknowledgments

*Badges*
  - [Shields.io](https://shields.io/)
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
  - [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)


<p align="right">
  <a href="#top"><b>Return</b></a>
</p>

---
