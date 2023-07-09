let url = `ws://${window.location.host}/ws/socket-server/`
const chatSocket = new WebSocket(url)

chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data)
    console.log('Data:', data)
    
    switch(data.type)
    {
        case 'chat_message':
            let messages = document.getElementById('messages')             
            messages.insertAdjacentHTML('beforeend', `<div>
                                    <p>${data.message}</p>
                                </div>`)
        break;
        case 'image':
          var img = document.getElementById("image");
          img.src = "data:image/png;base64," + data.message;  
        break;
        case 'runvar':
            var img = document.getElementById("runBtn");
           
            console.log(document.getElementById("runBtn"));
         
            if(data.message==="True")
            {
                var circle = document.querySelector('#Circle');

                circle.classList.remove('statusInactive')
                circle.classList.add('statusActive');
                //circle.style.fill = 'pink'; 
                //img.style.background="pink"
                //img.style.fill="pink"
                //img.setAttribute("fill", "red")
                console.log("pink")
            }
            else
            {
                var circle = document.querySelector('#Circle');
                circle.classList.remove('statusActive')
                circle.classList.add('statusInactive');

                img.style.fill="blue"
                //img.style.background="blue"
                console.log("blue")
            }
            break;
    }
    
}
let form = document.getElementById('form')
form.addEventListener('submit', (e)=> {
    e.preventDefault()
    let message = e.target.message.value 
    chatSocket.send(JSON.stringify({
        'message':message
    }))
    form.reset()
})
function buttonClick(Boundmethod,id)
{
    console.log('click!')
    chatSocket.send(JSON.stringify({
        'type':id,
        'message':"buttonclicked",
        'function': Boundmethod
    }))
}
