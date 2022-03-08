
let date = '14.02.2022'
let dateArray = date.split('.')
let newDate = new Date(dateArray[2], dateArray[1], dateArray[0])

 function getWeekday(){
  let options ={weekday: 'long'}
  let day = newDate.toLocaleDateString('ru-RU', options)
  day = day[0].toUpperCase() + day.slice(1);
  return day
 }

 function getWeek(){
 let xDate = dateArray[0]

 if (newDate.getDay() == 0){
 let yDay=7}
 else{yDay = newDate.getDay()}

 if ((xDate%7 - yDay) >= 0){
 let res = (xDate/7 |0) +2}
 else{
 return res = (xDate/7 |0) +1}
}

function getMonth(){
  let options = {month: 'long'}
  let month = newDate.toLocaleDateString('ru-RU', options)
  if (month.slice(-1) == 'ь' || month.slice(-1) == 'й'){
    month = month.replace(/.$/, 'я')
  } else{
    month = month+'а'
  }
  let res = month[0].toUpperCase() + month.slice(1)
  return res
}

function result(){
  // return getWeekday()+', '+getWeek()+' неделя '+getMonth()+' '+dateArray[2]+' года'
  console.log(getWeekday()+', '+getWeek()+' неделя '+getMonth()+' '+dateArray[2]+' года')
  console.log('hiiiiii')
}

result()
// <!-- getDayinfo('01.01.2022') Суббота, 1 неделя Января 2022 года -->
