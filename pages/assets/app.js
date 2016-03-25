function toggleUpdateFeedItem() {
    var updates = document.getElementsByClassName('item');

    if(updates.length > 5){
        for(var i = 5; i < updates.length; i++){
            updates[i].classList.toggle('hide')
        }
    }
}

toggleUpdateFeedItem();

document.getElementsByClassName('hide-link')[0].addEventListener('click', toggleUpdateFeedItem);
