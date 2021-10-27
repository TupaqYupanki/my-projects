function addElement (i, url, mini, row){
var newBut = document.createElement('input')
//var newPic = list[i].cloneNode(true)
var newPicUrl = list[i].querySelector('.cm-item-gallery > a > img').src
var newPic = document.createElement("img")
newPic.src = newPicUrl
newBut.type = 'checkbox'
newBut.id = 'a'+i
newBut.value = url
newBut.setAttribute('onclick','res(a'+i+')')

row.append(newPic)
row.appendChild(newBut)
row.appendChild(document.createElement('br'))
row.appendChild(document.createElement('br'))
//newDiv.appendChild(document.createElement('br'))
}

function res(id){
     if (id.checked){
      buf.push(id.value)
    }else{
      buf.pop(id.value)
    }
    result.innerText = buf
  }


buf = []
newDiv = document.createElement("div");
newDiv.style.border = 'solid 3px black'
newDiv.id = 'newDiv'
newDiv.style.width = '40%'
newDiv.style.height = '80%'
newDiv.style.marginLeft = '60%'
newDiv.style.marginTop = '125px'
newDiv.style.zIndex = '9999999'
newDiv.style.position = 'fixed'
newDiv.style.background = 'white'

newRow1 = document.createElement('div')
newRow1.style.width = '33%'
newRow1.style.height = '70%'
newRow1.style.float = 'left'
newDiv.append(newRow1)

newRow2 = document.createElement('div')
newRow2.style.width = '33%'
newRow2.style.height = '70%'
newRow2.style.float = 'left'
newDiv.append(newRow2)

newRow3 = document.createElement('div')
newRow3.style.width = '33%'
newRow3.style.height = '70%'
newRow3.style.float = 'left'
newDiv.append(newRow3)

rowCounter = 0

originalDiv = document.getElementsByClassName('tygh-content')[0]
originalDiv.parentNode.insertBefore(newDiv, originalDiv)

result = document.createElement('span')
result.style.fontSize = '14px'

wraper = document.getElementsByClassName('ty-product-thumbnails')
list = wraper[0].querySelectorAll('.owl-carousel > .owl-wrapper-outer > .owl-wrapper > .owl-item')

for (i in list){
    if(i < list.length){
mini = list[i].querySelector('.cm-item-gallery > .cm-gallery-item > .ty-pict').src
url = mini.split('thumbnails/55/55/')[0]+mini.split('thumbnails/55/55/')[1].split('.jpg')[0]+'.jpg'
if (rowCounter < 8){
  row = newRow1
addElement(i, url, mini, row)
rowCounter=rowCounter+1
}else if(rowCounter >7 && rowCounter <16){
  row = newRow2
  addElement(i, url, mini, row)
  rowCounter=rowCounter+1
}else{
  row = newRow3
  addElement(i, url, mini, row)
}

    }
    newDiv.appendChild(result)
}
