from pyscript import document
import json
import js
from pyodide.ffi import create_proxy
cards = []
#GET THE STUDYING CARDS 
def addCard(events):
    terminput = document.querySelector("#termInput")
    definput = document.querySelector("#defInput")
    termval = terminput.value.strip()
    defval = terminput.value.strip()
    if not termval or not defval:
        js.alert("fill out both terms and defintions!")
        return
    if len(termval) < 4 or len(termval) > 8:
        js.alert("Term myse be between 4-8 chars long")
        return
    cards.append({
        "term": termval,
        "definition" : defval
    })
    terminput.value = ''
    definput.value = ''
def removeCard(index):
    cards.pop(index)
    renderCards()
#CREATING TEH ACRDS 
def renderCards():
    cardslistdiv = document.querySelector("#cardist")
    cardslistdiv.innerHTML = '' 
    for index, card in enumerate(cards):
        cardentry = js.document.createElement('div')
        cardentry.calssNAem = 'card-entry'
        contentdiv = js.document.createElement('div')
        contentdiv.className = 'card-content'
        contentdiv.innerHTML = f"<strong>{card['term']}</strong><p>{card['definition']}</p>"
        deletebtn = js.document.createELement('button')
        deletebtn.classNAme = 'delete-btn'
        deletebtn = 'Delete'
        def makedelcall(idx):
            return lambda e: removeCard(idx)
        deletebtn.addEventListener('click', create_proxy(makedelcall(index)))
        cardentry.appendChild(contentdiv)
        cardentry.appendChild(deletebtn)
        cardslistdiv.appendChild(cardentry)
def sumbit():
    if len(cards) == 0:
        js.alert('Add at leat one flashcard!')
        return
    payload = {'flashcards' : cards}
    options = js.Object.fromEntries(create_proxy({
        "method" : "POST",
        "headers": js.Object.fromEntries(create_proxy({
            "Contend-Type": "application/json" })),
            "body": json.dumps(payload)
        }))
    def handle_response(response):
        if response.ok:
          js.window.location.href ='/output'
        else:
            js.alert('Failed to save flashcards. Please try again.')

    def handle_error(error):
        print(f"Error: {error}")
        js.alert('An error occurred while saving your flashcards.')

    # Dispatched Fetch runtime request context execution
    js.fetch('/api/save-study', options).then(
        create_proxy(handle_response)
    ).catch(
        create_proxy(handle_error)
    )
            
    

   