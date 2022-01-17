// ==UserScript==
// @name         piccolo-script
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://piccolo-detki.ru/*
// @icon         https://www.google.com/s2/favicons?domain=piccolo-detki.ru
// @grant        none
// ==/UserScript==

//wait 2sec
await new Promise(r => setTimeout(r, 2000));

//function that create new elements: checkboxes and pictures
window.addElement = function (i, url, mini) {
    var newBut = document.createElement('input')
    var newPicUrl = list[i].querySelector('.cm-item-gallery > a > img').src
    var newPic = document.createElement("img")
    newPic.src = newPicUrl
    newBut.type = 'checkbox'
    newBut.id = 'a'+i
    newBut.value = url
    newBut.setAttribute('onclick','res(a'+i+')')

    //adding created elements to our newDiv
    newDiv.append(newPic)
    newDiv.appendChild(newBut)
}

//function for click on checkbox. onclick adding url to JS Object
window.res = function (id) {
     if (id.checked){
      buf[id.id] = id.value
      counter = counter + 1
      count.innerText = counter
      result.innerText = Object.values(buf)
    } else {
      delete buf[id.id]
      counter = counter - 1
      count.innerText = counter
      result.innerText = Object.values(buf)
    }

  }

//function for button that hide newDiv window
window.hid = function (){
  if (newDiv.style.visibility != 'hidden'){
    newDiv.style.visibility = 'hidden'
  }else{
    newDiv.style.visibility = ''
  }
}

//function for button that switch between comma and space
window.switchch = function (){
  if (result.innerText.includes(",")) {
    result.innerText = result.innerText.replaceAll(',', ' ')
  }else if (result.innerText.includes(" ")) {
    result.innerText = result.innerText.replaceAll(' ', ',')
  }
  }

//function created checkbox that toggle all checkboxes in newDiv
window.toggle = function (source){
  checkboxes = newDiv.querySelectorAll('input')
  for (var i=0;i<checkboxes.length;i++){
      checkboxes[i].checked = source.checked;
      res(checkboxes[i])}
}

//checkbox that toggle or untoggle all checkboxes in newDiv
var toggleBut = document.createElement('input')
toggleBut.type = 'checkbox'
toggleBut.setAttribute('onclick','toggle(this)')
document.getElementsByClassName('header-phone')[0].append(toggleBut)

var counter = 0 //count chekboxed elements

//element span with urls
var result = document.createElement('span')
result.style.fontSize = '14px'

//element span that display counter of chexboxed elements
var count = document.createElement('span')
count.style.fontsize = '20px'

//creating element Object for result
var buf = {}

//creating element div that will contain img and checkboxes
var newDiv = document.createElement("div")
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

//creating button for hiding or showing our div
var hidButn = document.createElement('button')
hidButn.style.width = '30px'
hidButn.style.height = '30px'
hidButn.style.float = 'right'
hidButn.setAttribute('onclick',"hid()")
document.getElementsByClassName('header-phone')[0].append(hidButn)

//creating button for switching between comma and space
var switchButn = document.createElement('button')
switchButn.style.width = '30px'
switchButn.style.height = '30px'
switchButn.style.marginTop = '30px'
switchButn.style.background = 'aquamarine'
switchButn.setAttribute('onclick', "switchch()")
document.getElementsByClassName('header-phone')[0].append(switchButn)



//finding element by class name for adding to that element our newDiv
var originalDiv = document.getElementsByClassName('tygh-content')[0]
originalDiv.parentNode.insertBefore(newDiv, originalDiv)

//finding div that contains elements for parsing
var wraper = document.getElementsByClassName('ty-product-thumbnails')

//checking wraper contain 'owl-carousel' element or 'cm-item-gallery'
if (wraper[0].querySelectorAll('.owl-carousel > .owl-wrapper-outer > .owl-wrapper > .owl-item').length != 0){
var list = wraper[0].querySelectorAll('.owl-carousel > .owl-wrapper-outer > .owl-wrapper > .owl-item')
}else{var list = wraper[0].querySelectorAll('.cm-item-gallery')}

//waiting another 5sec
await new Promise(r => setTimeout(r, 5000));

//fill our div with chekboxes and img
for (var i in list){
if (i < list.length) {
  var mini = list[i].querySelector('.cm-item-gallery > .cm-gallery-item > .ty-pict').src
  var url = mini.split('thumbnails/55/55/')[0]+mini.split('thumbnails/55/55/')[1].split('.jpg')[0]+'.jpg'
  addElement(i, url, mini)
} else {//adding count and result span
    newDiv.appendChild(document.createElement('br'))
    newDiv.appendChild(count)
    newDiv.appendChild(document.createElement('br'))
    newDiv.appendChild(result)
    break
  }
}
