let btns = document.getElementByClassName('addtocart')
for(let i = 0;i < btns.length; i++){
    btns[i].addEventListener('click', function(e){
        let product_id = e.target.dataset.product
        let action = e.target.dataset.action
        console.log(product_id)
        if(user=='AnonymousUser'){
        console.log('you are not signed in')
        }

        else{
        addtocart(product_id,action)
        }
    })
}