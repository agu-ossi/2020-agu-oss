# Best Practices for Developing and Sustaining Your Open-Source Research Software

Material for the workshop at the AGU 2020 Fall Meeting.

**Conveners:**
Rene Gassmoeller,
Lindsey Justine Heagy,
Christopher Bane Sullivan,
Leah Wasser

|    |Info|
|---:|:---|
|Time|Dec 17th / 08:00 - 11:00 PST|
|Workshop ID|SCIWS13|
|Workshop access| [Program + Zoom Link](https://agu.confex.com/agu/fm20/meetingapp.cgi/Session/103714)|
|Shared notes| [Google Docs](https://docs.google.com/document/d/1KrBm1FEnd7gcnscCXyWP_-NEKIDcvgsy3Gfo56pLPpE/edit?usp=sharing)|
|Slides| [Slides](https://docs.google.com/presentation/d/1dvtxWFthZA6S1ZGs2OetkesyIB_hPEAjFn7pyo2iz6o/edit?usp=sharing)|
|Pre-Workshop survey| [Expectations](https://forms.gle/tkMyLBx67Jdt6yePA)|
|Post-Workshop survey| [Feedback](https://forms.gle/WhDCnda618qpMywN6)|

## Description
test change

Modern research software is the basis of scientific progress in geophysics by supporting data collection, data analysis, and numerical simulation. These codes span the range from small one-off scripts developed by individual researchers up to large packages with thousands of users. While there is increasing awareness about best programming practices, scientists are rarely prepared to scale their codes into team projects developed by  larger communities. However, growing a sustainable software project and the community of practice that surrounds it is a prerequisite to make scientific software development more efficient and research more reproducible.

The open-source community has established modern best-practices for developing reliable software, publishing that software, forming communities around the code, and finding sustainable ways to maintain them over time. This hands-on half-day workshop is aimed at scientists currently developing their own software of any size. The participants will apply a workflow for developing and managing open-source research codes following best-practices. We will discuss licensing and privacy considerations for open-source projects in a scientific context, briefly review version control with git and hosting projects online, and teach how to automatically test and efficiently document code. Furthermore, we will discuss how to grow projects and manage communities around it. The course material is independent of programming language or scientific discipline. By the end of this workshop participants will be able to apply the gained knowledge directly to their own projects and create more sustainable research software.

## Learning Objectives

Our aim with this workshop is for participants to: 

1. Learn about modern best-practices for developing, testing, documenting, and publishing research software that promote accessibility, reusability, and reproducibility. 
2. Gain hands-on experience with open-source software development tools available to researchers including Jupyter (for sharing), git (versioning), GitHub (collaboration), ReadTheDocs (documentation), and Travis CI (testing).
3. Learn basic concepts of software project management like the life cycle of scientific software, defining a target audience, developing a project mission and vision, building a welcoming community, and approaching scientists uncomfortable with sharing their research software.

## Tentative Agenda

During the workshop, we'll introduce these topics by working through an example.

| Duration (min) | Topic | Tools |
|:--------------:|:------|:------|
| 5 | Introduction, explain workshop resources and format | Zoom, Github |
| 20 | Motivations for community research software and its technical and social challenges. Software as a project, not a collection of files| |
| 15 | Introduce the example we will work through | Github |
| 15 | Practical review of version control with git and setting up an online repository on GitHub with the provided example project | Github, git |
| 5 | Break | |
| 10 | Managing communication and building a welcoming community | |
| 35 | Why and how to write tests | Github Actions |
| 15 | How to set up continuous integration services to automate tests | Github Actions |
| 5 | Break | |
| 15 | Importance of documentation and naming conventions. How to write and publish documentation. | Github Pages |
| 15 | Q&A discussion in breakout groups. | |
| 5 | Feedback Survey | |

## *Before* the workshop

Please check this page again before the workshop.

- Fill out our [Pre-Workshop survey](https://forms.gle/tkMyLBx67Jdt6yePA), this helps us tune the content.
- If you do not already have one, set up a free [GitHub account](https://github.com/).
- **Technical requirements**: None (well, a working Zoom, browser, and AGU login). The workshop will be based on cloud services and any operating system will work.

## *After* the workshop

Since the time allocated for the workshop does not allow to cover scientific
software development in its entirety, we provide links to some alternatives and
guides to extend and deepen some of the taught concepts.

## Resources

- **Version control with Git:**
  - [Git - the simple guide](http://rogerdudler.github.io/git-guide/)
  - [Git Cheat Sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
  - [Earth Data Science Guide to Git](https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/version-control/ )
- **Software packing:**
  - [The Hitchhiker's Guide to packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/)
- **[Software licensing](https://choosealicense.com/)**
- **[Code of Conduct](https://www.contributor-covenant.org/)**
  
### Alternatives to the tools presented

- **Version control**
  - [GitLab](https://www.gitlab.com): Version control for with private repositories and for your own server

- **Continous Integration**
  - [CircleCI](https://circleci.com): Alternative to Travis (https://circleci.com/circleci-versus-travisci/).
  - [Jenkins](https://github.com/jenkinsci/jenkins): Continuous integration on your own server. Might come in handy, for computationally more demanding software tests.

- **Documentation**
  - [MkDocs](https://www.mkdocs.org): Fast and simple project documentation using Markdown.
  - [ReadTheDocs](https://readthedocs.org/): Free hosting of documentation, Linked to Github.
  - [Sphinx](https://www.sphinx-doc.org/en/master/): Python documentation generator
  - [Doxygen](https://www.doxygen.nl): Multi-language documentation generator.

## Recording of AGU 2018 (slightly different focus)

[![recording-AGU](https://img.youtube.com/vi/Ck3f8Dbk98U/0.jpg)](https://youtu.be/Ck3f8Dbk98U)

Workshop - AGU 2020

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
