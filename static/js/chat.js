let location = window.location
let wsStart = 'ws://'



if (location.protocol === 'https'){
    wsStart = 'ws://'
}

let endpoint = wsStart + location.host + location.pathname


var socket = new WebSocket(endpoint)

socket.onopen = async function()