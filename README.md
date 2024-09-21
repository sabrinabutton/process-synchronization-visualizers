# Process Synchronization Visualizers

This repository contains the implementation of the following process synchronization simulators:

- [Peterson's Algorithm](https://en.wikipedia.org/wiki/Peterson%27s_algorithm)
- [Test and Set](https://en.wikipedia.org/wiki/Test-and-set)
- [Semaphore](<https://en.wikipedia.org/wiki/Semaphore_(programming)>)

These are not simulators, but rather lighteweight implementations of the algorithms mentioned above, with visual demonstrations. The time clocking in the visual demonstrations is not accurate, but it is there to give you an idea of how the algorithms work.

I developed this project to help me understand how these algorithms work for my operating systems course (ELEC 377 at Queen's University). I hope it helps you too.

Copyright Sabrina Button - 2024

# Usage

To run the visualizers, you need to have Python 3 installed on your machine. You can download it [here](https://www.python.org/downloads/).

`python petersons-critical-section-visualizer.py`

`python test-and-set-visualizer.py`

`python semaphore-visualizer.py`

Note that I wasn't able to kill the threads in any of the visualizers, so you will have to close the window to stop the simulation.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Contributing

If you would like to contribute to this project, please open an issue or a pull request. I would love to hear your feedback (and maybe make the visualizations more accurate, and also kill the threads).
