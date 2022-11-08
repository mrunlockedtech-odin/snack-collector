const dateInput = document.getElementById('id_purchase_date')

const picker = MCDatepicker.create({
  el: '#id_purchase_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener("click", (evt) => {
  picker.open()
})