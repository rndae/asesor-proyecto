## todo bien
* greet
  - utter_how_can_i_help
* inform
  - utter_ask_favorite_subject
* info_area{"area":"Matemáticas"}
  - action_project_search
  - utter_project
* pleased
  - utter_completed

## todo bien pero no satisfecho a la primera
* greet
  - utter_how_can_i_help
* inform
  - utter_ask_favorite_subject
* info_area{"area":"Matemáticas"}
  - action_project_search
  - utter_project
* not_pleased
  - action_project_search
  - utter_project
  - utter_ask_if_ok
* pleased
  - utter_completed

## de comienzo el area
* info_area{"area":"Matemáticas"}
  - action_project_search
  - utter_project
* not_pleased
  - action_project_search
  - utter_project
  - utter_ask_if_ok
* pleased
  - utter_completed

## segunda no
* greet
  - utter_how_can_i_help
* inform
  - utter_ask_favorite_subject
* inform_undecided_level_2 
  - utter_ask_least_disliked
* info_area{"area":"Matemáticas"}
  - action_project_search
  - utter_project
* pleased
  - utter_completed

## segunda no, tercera no, cuarta no
* greet
  - utter_how_can_i_help
* inform
  - utter_ask_favorite_subject
* inform_undecided_level_2
  - utter_ask_least_disliked
* inform_undecided_level_3
  - utter_ask_select_no_least_disliked
* info_area{"area":"Matemáticas"}
  - action_project_search
  - utter_project
* pleased
  - utter_completed

## segunda no, tercera no, cuarta no, quinta no
* greet
  - utter_how_can_i_help
* inform
  - utter_ask_favorite_subject
* inform_undecided_level_2
  - utter_ask_least_disliked
* inform_undecided_level_3
  - utter_ask_select_no_least_disliked
* inform_undecided_level_4
  - action_project_search_random
  - utter_recommend_anyway
* pleased
  - utter_completed

## otro proyecto pero pleased
* greet
  - utter_how_can_i_help
* inform
  - utter_ask_favorite_subject
* info_area{"area":"Matemáticas"}
  - action_project_search
  - utter_project
* not_pleased
  - action_project_search
  - utter_project
  - utter_ask_if_ok
* pleased
  - utter_completed

## otro proyecto pero unpleased
* greet
  - utter_how_can_i_help
* inform
  - utter_ask_favorite_subject
* info_area{"area":"Matemáticas"}
  - action_project_search
  - utter_project
* not_pleased
  - action_project_search
  - utter_project
  - utter_ask_if_ok
* not_pleased
  - action_project_search
  - utter_project
  - utter_ask_if_ok
* pleased
  - utter_completed

## bot challenge
* bot_challenge
  - utter_iamabot

## bot troll
* troll
  - utter_goodbye

## New Story

* greet
    - utter_how_can_i_help
* inform
    - utter_ask_favorite_subject
* info_area{"area":"matematicas"}
    - slot{"area":"matematicas"}
    - slot{"area":"matematicas"}
    - action_project_search
    - utter_project
* deny
    - utter_completed
* greet
    - utter_how_can_i_help
* inform
    - utter_ask_favorite_subject
* info_area{"area":"Matemáticas"}
    - slot{"area":"Matemáticas"}
    - slot{"area":"Matemáticas"}
    - action_project_search
    - utter_project
* info_area{"area":"gracias"}
    - slot{"area":"gracias"}
    - slot{"area":"matematicas"}
    - slot{"area":"Matemáticas"}
    - slot{"area":"gracias"}
    - utter_completed
* greet
    - utter_how_can_i_help
* inform
    - utter_ask_favorite_subject
* info_area{"area":"Química"}
    - slot{"area":"Química"}
    - slot{"area":"Química"}
    - action_project_search
    - utter_project
* deny
    - utter_completed
* greet
    - utter_how_can_i_help
* inform
    - utter_ask_favorite_subject
* info_area{"area":"Física"}
    - slot{"area":"Física"}
    - slot{"area":"Física"}
    - action_project_search
    - utter_project
* info_area{"area":"gracias"}
    - slot{"area":"gracias"}
    - slot{"area":"matematicas"}
    - slot{"area":"Matemáticas"}
    - slot{"area":"gracias"}
    - slot{"area":"Química"}
    - slot{"area":"Física"}
    - slot{"area":"gracias"}
    - utter_completed
* greet
    - utter_how_can_i_help
* inform
    - utter_ask_favorite_subject
* info_area{"area":"maTEmátics"}
    - slot{"area":"maTEmátics"}
    - slot{"area":"maTEmátics"}
    - action_project_search
    - utter_project
* info_area{"area":"gracias"}
    - slot{"area":"gracias"}
    - slot{"area":"matematicas"}
    - slot{"area":"Matemáticas"}
    - slot{"area":"gracias"}
    - slot{"area":"Química"}
    - slot{"area":"Física"}
    - slot{"area":"gracias"}
    - slot{"area":"maTEmátics"}
    - slot{"area":"gracias"}
    - utter_completed
* greet
    - utter_how_can_i_help
* inform
    - utter_ask_favorite_subject
* info_area{"area":"mateMatics"}
    - slot{"area":"mateMatics"}
    - slot{"area":"mateMatics"}
    - action_project_search
    - utter_project
* pleased{"area":"gracias"}
    - slot{"area":"gracias"}
    - utter_completed

## New Story

* greet
    - utter_how_can_i_help
* greet
    - utter_how_can_i_help
* inform
    - utter_ask_favorite_subject
* info_area{"area":"matematicas"}
    - slot{"area":"matematicas"}
    - slot{"area":"matematicas"}
    - action_project_search
    - slot{"project":"Impresión 3D"}
    - slot{"area":"Matemáticas"}
    - utter_project
* info_area{"area":"Física"}
    - slot{"area":"Física"}
    - slot{"area":"Física"}
    - action_project_search
    - slot{"project":"Nuevos Materiales"}
    - slot{"area":"Física"}
    - utter_project
* info_area{"area":"Química"}
    - slot{"area":"Química"}
    - slot{"area":"Química"}
    - action_project_search
    - slot{"project":"Grafeno (Como Ejemplo De Nuevos Materiales Con Propiedades Excepcionales)"}
    - slot{"area":"Química"}
    - utter_project
* pleased
    - utter_completed
* goodbye
    - slot{"area":"matematicas"}
    - slot{"area":"Física"}
    - slot{"area":"Química"}
    - utter_goodbye
