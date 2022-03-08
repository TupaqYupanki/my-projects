// <!-- getDayinfo('01.01.2022') Суббота, 1 неделя Января 2022 года -->
function getDayinfo(date){
let dateArray = date.split('.')
let newDate = new Date(dateArray[2], parseInt(dateArray[1])-1, dateArray[0])

function getWeekday(){
  let options = {weekday: 'long'}
  let day = newDate.toLocaleDateString('ru-RU', options)
  day = day[0].toUpperCase() + day.slice(1)
  return day
}

function getWeek(){
 let date = dateArray[0]
 if (newDate.getDay() == 0){
  weekday = 7
 }else{
  weekday = newDate.getDay()
 }

 if ((date%7 - weekday) >= 0){
  res = (date/7 |0) +2}
 else{
  res = (date/7 |0) +1}
 return res
}

function getMonth(){
  let options = {month: 'long'}
  let month = newDate.toLocaleDateString('ru-RU', options)
  month = month[0].toUpperCase() + month.slice(1)

  if (month.slice(-1) == 'ь' || month.slice(-1) == 'й'){
    month = month.replace(/.$/, 'я')
  } else{
    month = month+'а'
  }
 return month
}

return(getWeekday()+', '+getWeek()+' неделя '+getMonth()+' '+dateArray[2]+' года')
}
