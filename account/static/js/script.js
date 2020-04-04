// save-delete btns
let save_to_album_btns = document.getElementsByClassName('save_to_album');

async function make_request(url_mode, img_name) {
    let url = url_mode + img_name;
    let response = await fetch(url);
    let data = await response.text();
    return data;
}

function change_btn_mode(btn_id, handler, del_color_cls, new_color_cls, text) {
    let btn =  document.getElementById('images/'+btn_id);
    btn.onclick = handler;
    // style
    btn.classList.remove(del_color_cls);
    btn.classList.add(new_color_cls);
    btn.innerText = text;
    btn.blur();
}

function save_img(event) {
    try {
        let img_name = String(event.currentTarget.id).split('/')[1];
        let data = make_request('save_img/', img_name);
        event.preventDefault()
        data.then(data => {
            if (data == 'saved') {
                change_btn_mode(img_name, delete_img, 'btn-succes', 'btn-danger', 'Del from Album');
            } else {
                console.log('incorrect img name');
            }
        });
    } catch (e) {
        console.error(e);
    }
}

function delete_img(event) {
    try {
        let img_name = String(event.currentTarget.id).split('/')[1];
        let data = make_request('delete_img/', img_name);
        event.preventDefault()
        data.then(data => {
            if (data == 'deleted') {
                change_btn_mode(img_name, save_img, 'btn-danger', 'btn-success', 'Save to Album');
            } else {
                console.log('incorrect img name');
            }
        });
    } catch (e) {
        console.error(e);
    }
}

for (let btn of save_to_album_btns) {
    btn.onclick = save_img;
}

// del from album btns
let del_from_album_btns = document.getElementsByClassName('del_from_album');

for (let btn of del_from_album_btns) {
    btn.onclick = delete_img;
}

// full screen btns
let full_screen_btns = document.getElementsByClassName('full_screen_btn');

let modal = document.getElementById('modal_img_container');

function display_img(event) {
    let btn = event.currentTarget;
    let parent_el = btn.parentElement;
    let img_src = parent_el.firstElementChild.id;
    modal_img.src = "/static/" + img_src;
    modal.style.display = "block";
    btn.blur();
}

for (let btn of full_screen_btns) {
    btn.onclick = display_img;
}

// close modal
try{
    let btn_close_modal = document.getElementById('close_modal');

    btn_close_modal.onclick = function() {
        modal.style.display = "none";
    }
} catch (e) {
    console.log("modal window doesnt exist yet");
}

// delete message
let close_msg_btn = document.getElementById('close');
let msg_elem = document.getElementsByClassName('success');

if ( msg_elem.length == 0){
    msg_elem = document.getElementsByClassName('error');
}

function close_msg(event) {
    for (let msg of msg_elem) {
        msg.remove();
    }
}

if (close_msg_btn) {
    close_msg_btn.onclick = close_msg;
}

if (window.screen.width < 450 && String(document.location.pathname).split('/')[1] != 'account') {
    if (full_screen_btns.length > 1) {
        // more than 1 card
        let footer = document.getElementById("footer");
        footer.classList.remove("navbar");
        footer.classList.remove("fixed-bottom");
    }
} 
