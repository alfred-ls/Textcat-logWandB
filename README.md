<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy & wandb Project: 
## Use Case 02 Text Classification BBC & NG news
+ Using Weights & Biases for logging of training experiments

A textcat project for spaCy v3. The project data comes from kaggle: 
+ BBC (https://www.kaggle.com/hgultekin/bbcnewsarchive)
+ NG (https://www.kaggle.com/salmaelanigri/doc-class)


Label scheme (3 combined labels for 1 component):

| Component | Labels |
| --- | --- |
| **`textcat`** | `tech`, `sport`, `entertainment` |


## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows.

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `convert` | Convert the data to spaCy's binary format |
| `train` | Train the textcat model and log the results via wandb |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model as a pip package |
| `visualize-model` | Visualize the model's output interactively using Streamlit |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `convert` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project.

| File | Source | Description |
| --- | --- | --- |
| [`assets/UC2_train_prodigy.jsonl`](assets/UC2_train_prodigy.jsonl) | Local | Demo training data |
| [`assets/UC2_eval_prodigy.jsonl`](assets/UC2_eval_prodigy.jsonl) | Local | Demo development data |


### 💯 Insights

Some project insights and plots.

![MetricsFor_modeltraining](https://user-images.githubusercontent.com/52454409/133236738-85ee2c42-5ef1-494a-ad46-b8319595b2f4.png)

![MetricsFor_modelevaluation](https://user-images.githubusercontent.com/52454409/133237146-6e2ae384-c908-4813-8d2e-9f85e8b49862.png)

![AccuracyVSRuntime_modeltraining](https://user-images.githubusercontent.com/52454409/133237193-49b8e4a4-a5f5-4224-a6c2-27f6bf74c883.png)


<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
