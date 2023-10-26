class Chatbox{
    constructor() {
        this.args = {
            openButton: document.querySelector(".chatbox__button"),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }
        this.state = false;
        this.messages = [];
    }
    display(){
        const {openButton, chatBox, sendButton} = this.args;
        openButton.addEventListener("click", () => this.toggleState(chatBox))
        sendButton.addEventListener("click", () => this.onSendButton(chatBox))

        const node = chatBox.querySelector("input");
        node.addEventListener("keyup", ({key}) => {
            if(key === "Enter"){
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox){
        this.state = !this.state;

        if(this.state){
            chatbox.classList.add("chatbox--active")
        }
        else {
            chatbox.classList.remove("chatbox--active")
        }
    }
    onSendButton(chatbox){
        let textField = chatbox.querySelector("input");
        let first_text = textField.value
        if (first_text === ""){
            return;
        }
        let first_msg = {name: "User", message: first_text}
        this.messages.push(first_msg);
        // 'http://127.0.0.1:5000/predict'
        fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            body: JSON.stringify({message: first_text}),
            mode: "cors",
            headers: {
                "Content-Type": "application/json"
            },
          })

          .then(r => r.json())
          .then(r => {
            let second_msg = {name: "Sam", message: r.answer};
            this.messages.push(second_msg);
            this.updateText(chatbox);
            textField.value = ""
        });
    }
    updateText(chatbox){
        let html = "";
        this.messages.slice().reverse().forEach(function(item, index){
            if (item.name === "Sam"){
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else{
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });
        const chatmessage = chatbox.querySelector(".chatbox__messages");
        chatmessage.innerHTML = html;

    }
}
const chatbox = new Chatbox();
chatbox.display();













