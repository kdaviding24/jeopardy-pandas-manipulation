import pandas as pd
#pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')
#print(jeopardy.info())

#cleans column names

jeopardy_columns = [i.strip() for i in list(jeopardy)]


#print(jeopardy_columns)

jeopardy.columns = jeopardy_columns

#returns a list of questions that use a Keyword from a list of keywords

def grab_questions_by_list(df, list):
  questions = []
  for a in list:
    for b in df['Question']:
      if b.upper().split().count(a.upper()) >= 1:
        questions.append(b)
  return questions

#next four commands change the value column from a string to a float. Could have put it in a function and condensed commands.

jeopardy['Value'] = jeopardy.apply(lambda x: x.Value.strip('$'), axis = 1)

jeopardy['Value'] = jeopardy.apply(lambda x: x.Value.split(','), axis = 1)

jeopardy['Value'] = jeopardy.apply(lambda x: ''.join(x.Value), axis = 1)

jeopardy['Value'] = jeopardy.apply(lambda x: float(x.Value) if x.Value != "None" else x.Value, axis = 1)

#returns the average value of a question based on a keyword(s)

def avg_value_by_topic(df, list):
 return round(df[(df.Question.isin\
(grab_questions_by_list\
(df,list))) &\
(df.Value != 'None')].Value.mean(),2)

# returns number of how many times a answer is used based on a keyword and the answer itself
def nunique_answers_per_topic(df, topic):
   questions = []
   for b in df['Question']:
    if b.upper().split().count(topic.upper()) >= 1:
      questions.append(b)
   answers = []
   for i in list(df[df.Question.isin(questions)].Answer):
    answers.append(i.upper())

   answer_and_count = []
   for answer in answers:
    if answer not in answer_and_count:
      answer_and_count.append([answers.count(answer), answer.upper()])
   return answer_and_count

#update for answers count based on keyword
def update_nunique_answers_per_topic(df, topics_list):
  print(df[df.Question.isin\
(grab_questions_by_list\
(df, topics_list))].Answer.value_counts())

#unique_answers_king_questions = nunique_answers_per_topic(jeopardy, 'king')

#print(unique_answers_king_questions)

#print(jeopardy.Category.nunique())
#print(len(jeopardy.Category))



#print(king_england_question_avg_value)


