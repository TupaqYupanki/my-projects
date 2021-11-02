function addElement (i, url, mini){
var newBut = document.createElement('input')
var newPicUrl = list[i].querySelector('.cm-item-gallery > a > img').src
var newPic = document.createElement("img")
newPic.src = newPicUrl
newBut.type = 'checkbox'
newBut.id = 'a'+i
newBut.value = url
newBut.setAttribute('onclick','res(a'+i+')')

newDiv.append(newPic)
newDiv.appendChild(newBut)
}

function res(id){
     if (id.checked){
      buf[id.id] = id.value
      counter = counter + 1
      count.innerText = counter
      result.innerText = Object.values(buf)
    }else{
      delete buf[id.id]
      counter = counter - 1
      count.innerText = counter
      result.innerText = Object.values(buf)
    }

  }

function hid(){
  if (newDiv.style.visibility != 'hidden'){
    newDiv.style.visibility = 'hidden'
  }else{
    newDiv.style.visibility = ''
  }
}

buf = {}
newDiv = document.createElement("div");
newDiv.style.border = 'solid 3px black'
newDiv.id = 'newDiv'
newDiv.style.width = '60%'
newDiv.style.marginLeft = '20%'
newDiv.style.marginTop = '125px'
newDiv.style.zIndex = '9999999'
newDiv.style.position = 'fixed'
newDiv.style.background = 'white'
newDiv.style.flex = 'auto'
newDiv.style.padding = '10px';
newDiv.style.visibility = 'hidden'

hidButn = document.createElement('button')
hidButn.style.width = '30px'
hidButn.style.height = '30px'
hidButn.style.float = 'right'
hidButn.setAttribute('onclick',"hid()")
document.getElementsByClassName('header-phone')[0].append(hidButn)

rowCounter = 0
counter = 0

originalDiv = document.getElementsByClassName('tygh-content')[0]
originalDiv.parentNode.insertBefore(newDiv, originalDiv)

result = document.createElement('span')
result.style.fontSize = '14px'

count = document.createElement('span')
count.style.fontsize = '20px'

wraper = document.getElementsByClassName('ty-product-thumbnails')
if (wraper[0].querySelectorAll('.owl-carousel > .owl-wrapper-outer > .owl-wrapper > .owl-item').length != 0){
list = wraper[0].querySelectorAll('.owl-carousel > .owl-wrapper-outer > .owl-wrapper > .owl-item')
}else{list = wraper[0].querySelectorAll('.cm-item-gallery')}
for (i in list){
    if(i < list.length){
    mini = list[i].querySelector('.cm-item-gallery > .cm-gallery-item > .ty-pict').src
    url = mini.split('thumbnails/55/55/')[0]+mini.split('thumbnails/55/55/')[1].split('.jpg')[0]+'.jpg'
    addElement(i, url, mini)
    }else{
            newDiv.appendChild(document.createElement('br'))
            newDiv.appendChild(count)
            newDiv.appendChild(document.createElement('br'))
            newDiv.appendChild(result)
            break
         }
}
