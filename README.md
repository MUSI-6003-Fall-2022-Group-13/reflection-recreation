# Reflection Recreation

A recreation/reinterpretation of Brian Eno's "Reflection".

Group 13 final project for MUSI-6003.

## Running the Max project

First, run the Python script to generate and send MIDI notes over OSC:

```shell
$ pip install -r ReflectionRecreation/data/requirements.txt
$ python ReflectionRecreation/other/main.py
```

Open the [ReflectionRecreation](ReflectionRecreation) MaxMSP project.
(The project was created with Max v8.5 - please make sure your Max version is up-to-date!)

## Contributing

To contribute your changes:

1) Clone the git repo:
  `git clone git@github.com:MUSI-6003-Fall-2022-Group-13/reflection-recreation.git`
2) Open the project and make any changes.
3) Save the Max project with your changes.
4) Push your changes:
  - `git add .`
  - `git cm -m "A message describing your changes"`
  - `git push`
    - If somebody else has pushed some changes while you've been working, you may get an error here.
      In this case, it's probably going to be easiest to:
        - Save your changes somewhere (in a new branch, or just saving a separate Max patch)
        - `git pull` to get the upstream changes
        - Re-open the max project
        - Redo your changes in the Max patcher
        - Repeat step 5
