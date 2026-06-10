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
    defval = definput.value.strip()
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
    renderCards()
def removeCard(index):
    cards.pop(index)
    renderCards()
#CREATING TEH ACRDS 
def renderCards():
    cardslistdiv = document.querySelector("#cardsList")
    cardslistdiv.innerHTML = '' 
    for index, card in enumerate(cards):
        cardentry = js.document.createElement('div')
        cardentry.className = 'card-entry'
        contentdiv = js.document.createElement('div')
        contentdiv.className = 'card-content'
        contentdiv.innerHTML = f"<strong>{card['term']}</strong><p>{card['definition']}</p>"
        deletebtn = js.document.createElement('button')
        deletebtn.className = 'delete-btn'
        deletebtn.textContent = 'Delete'
        def makedelcall(idx):
            return lambda e: removeCard(idx)
        deletebtn.addEventListener('click', create_proxy(makedelcall(index)))
        cardentry.appendChild(contentdiv)
        cardentry.appendChild(deletebtn)
        cardslistdiv.appendChild(cardentry)
def submitCards(events):
    if len(cards) == 0:
        js.alert('Add at least one flashcard!')
        return
    payload = {'terms': [card['term'] for card in cards], 'definitions': [card['definition'] for card in cards]}
    options = create_proxy({
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(payload)
    })
    def handle_response(response):
        if response.status == 200:
            js.alert('Flashcards saved successfully!')
        else:
            print(f"Response status: {response.status}")
            js.alert(f'Failed to save flashcards. Status: {response.status}')

    def handle_error(error):
        print(f"Error: {error}")
        js.alert('An error occurred while saving your flashcards.')

    # Dispatched Fetch runtime request context execution
    js.fetch('/api/save-study', options).then(
        create_proxy(handle_response)
    ).catch(
        create_proxy(handle_error)
    )
            
    

   