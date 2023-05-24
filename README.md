# Embible

### In recent years we have witnessed an increase in ancient archaeological findings related to the Jewish nation. These findings are important for strengthening the identity, connection to culture, and history of the Jewish people.

Among these findings, a lot of the writings have been torn/faded over the years .
The model we are developing in our project aims to solve a masked language modeling (MLM) problem - completing missing (masked) sections in text. There may be several options for a missing section: missing words, a single word missing, a single letter missing or partial word. 

After reviewing a number of articles in the field and investigating the advantages and disadvantages of each model , we reached several conclusions: 
The disadvantage of these models is that most of them are good at predicting in the  English language and other languages they have been trained on (for example: Greek), but are not good at predicting in the Hebrew language.

There are models that predict whole missing words very well but predict worse for partial words that are missing, and vice versa.
Therefore, we developed an ensemble model trained using the Bible that takes the advantage of a model that knows how to predict whole missing words well and an advantage of a model that predicts partial missing words well. (The models on which our model is based, are models that we performed fine tuning on to improve their predictions).

During the research, we implemented metrics to evaluate and measure the quality of the prediction while checking for a different percentage of masked parts in text.
The model is a part of a system. A user will enter text with missing parts into the system. For the missing parts, the system will return several options, each option has a probability of completing the hidden part.

This is how we will help historians whose goal is to restore ancient Jewish scrolls and writings as their life's mission.


![alt text][(http://url/to/img.png](https://www.google.com/url?sa=i&url=https%3A%2F%2Fdeadsea.com%2Fhe%2F%25D7%259E%25D7%2590%25D7%259E%25D7%25A8%25D7%2599%25D7%259D-%25D7%2595%25D7%2598%25D7%2599%25D7%25A4%25D7%2599%25D7%259D%2F%25D7%2594%25D7%2599%25D7%25A1%25D7%2598%25D7%2595%25D7%25A8%25D7%2599%25D7%2594%2F%25D7%259E%25D7%2594%25D7%259F-%25D7%259E%25D7%2592%25D7%2599%25D7%259C%25D7%2595%25D7%25AA-%25D7%2599%25D7%259D-%25D7%2594%25D7%259E%25D7%259C%25D7%2597-%25D7%259C%25D7%259E%25D7%2593%25D7%2595-%25D7%25A2%25D7%2595%25D7%2593-%25D7%25A2%25D7%259C-%25D7%259E%25D7%2592%25D7%2599%25D7%259C%25D7%2595%25D7%25AA-%25D7%25A7%2F&psig=AOvVaw2v0MBxvIqUzDNf9D8FzJ3A&ust=1685051458723000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOD0tYD4jv8CFQAAAAAdAAAAABAD))

