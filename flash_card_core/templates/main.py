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
        document.querySelector("#get_term_out").innerHTML =  get_term_out
        print(get_term_out)

#GET THE DEFITION TERM
def get_definition():
    get_definition_html = document.querySelector("#item_input")
    user_definition = get_definition_html.value
    if user_definition.strip().upper() != "":
         get_definition_list.append(user_definition)
         get_definition_html.value = ""
    get_definition_out = "<ul>"
    for x in get_definition_list:
         get_definition_out += f"<li>{x}</li>"
    get_definition_out += "</ul>"
    document.querySelector("#get_definition_out").innerHTML = get_definition_out
    print(get_definition_out)

def combine(events):
     if len(get_term_list) != len(get_definition_list):
          document.querySelector("#flashcard").innerHTML = "Error"
          return 
     full_study = dict(zip(get_term_list,get_definition_list))


