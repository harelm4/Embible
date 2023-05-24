# Embible

Project Summary:
In recent years we have witnessed an increase in ancient archaeological findings related to the Jewish nation. These findings are important for strengthening the identity, connection to culture, and history of the Jewish people.

Among these findings, a lot of the writings have been torn/faded over the years .
The model we are developing in our project aims to solve a masked language modeling (MLM) problem - completing missing (masked) sections in text. There may be several options for a missing section: missing words, a single word missing, a single letter missing or partial word. 

After reviewing a number of articles in the field and investigating the advantages and disadvantages of each model , we reached several conclusions: 
The disadvantage of these models is that most of them are good at predicting in the  English language and other languages they have been trained on (for example: Greek), but are not good at predicting in the Hebrew language.

There are models that predict whole missing words very well but predict worse for partial words that are missing, and vice versa.
Therefore, we developed an ensemble model trained using the Bible that takes the advantage of a model that knows how to predict whole missing words well and an advantage of a model that predicts partial missing words well. (The models on which our model is based, are models that we performed fine tuning on to improve their predictions).

During the research, we implemented metrics to evaluate and measure the quality of the prediction while checking for a different percentage of masked parts in text.
The model is a part of a system. A user will enter text with missing parts into the system. For the missing parts, the system will return several options, each option has a probability of completing the hidden part.

This is how we will help historians whose goal is to restore ancient Jewish scrolls and writings as their life's mission.

