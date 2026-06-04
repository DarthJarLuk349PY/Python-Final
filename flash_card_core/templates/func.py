from pyscript import document

get_term_list = []
get_definition_list = []
full_study = {}

#GET THE STUDYING TERM
def get_term(x):
        get_term_html = document.querySelector("#item_input")
        user_term = get_term_html.value
        if user_term.strip() != "":
            get_term_list .append(user_term)
            get_term_html.value = ""
        get_term_out ="<ul>"
        for i in get_term_list :
            get_term_out += f"<li>{i}</li>"
        get_term_out += "</ul>"
        document.querySelector("#get_term_out").inerHTML =  get_term_out
        print(get_term_out)

#GET THE DEFITION TERM
def get_definition():
    get_definition_html = document.querySelector("#item_input")
    user_definition = get_definition_html.value
    if user_definition.strip().upper() != "":
         get_definition_list.append(user_definition)
         get_definition_html.value = ""
    get_definition_out = "</ul>"
    for x in get_definition_list:
         get_definition_out += f"<li>{x}</li>"
    get_definition_out += "</ul>"
    document.querySelctor("#get_definition_out").inerHTML = get_definition_out
    print(get_definition_out)


def combine(events):
     if len(get_term_list) != len(get_definition_list):
          document.querySelector("#flashcard").innerHTML = "Errror"
          return 
     full_study = dict(zip(get_term_list,get+get_definition_list))
     show_next_card()


def show_next_card():
     global current_index
     if current_index 


def check_if_right():
#SOMTHING ALONG THE LINES OF THIS WERE USER ENTERS IF THEY QUESTIO IS RIGHT OT NOT
#THEN THE TAKES AS BOOL VARIABLE??? (IN PROGRESS)
    global current_index, full_study

    if not full_study:
         document.query Seclotor("#feeedback").innerHTML = "please click comine to start "
         return
    
    user_answer = document.querySelctor("#user_answee_input").value.strip()
    c_term = get_term_list[current_index]
    c_defintion = full_study[current_term]
    if current_index >= len(get_term_list):
         document.querySelector("#flashcar_display").innerHTML = "Wrong"
         current_index += 1
         show_next_card()
     else:
         document.quesrySelceto("#feedback").innerHTML = "Incorrect, Try Agian" 
