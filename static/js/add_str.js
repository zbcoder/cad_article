var table_counter = 1

function add_str(table_id){
    let qs_tr = document.querySelectorAll('tr')[table_counter].children
    tr_text = document.querySelectorAll('tr')[table_counter].innerHTML
    tr = document.createElement('tr')
    tr.innerHTML = tr_text
    document.querySelector('tbody').appendChild(tr)
    table_counter += 1
    
    let new_tr = document.querySelectorAll('tr')[table_counter].children
    
    new_tr.item(3).querySelector('input').value = qs_tr.item(3).querySelector('input').value
    // new_tr.item(4).querySelector('input').value = qs_tr.item(4).querySelector('input').value
    // new_tr.item(5).querySelector('input').value = qs_tr.item(5).querySelector('input').value
    // new_tr.item(6).querySelector('input').value = qs_tr.item(6).querySelector('input').value
    tmp_oper_number = parseInt(qs_tr.item(0).querySelector('input').value, 10) + 10
    
    let save_input = new_tr.item(0).querySelector('input');
    new_tr.item(0).innerHTML = ''
    new_tr.item(0).innerHTML = tmp_oper_number.toString().padStart(3, '0') 
    new_tr.item(0).appendChild(save_input)
    save_input.value = tmp_oper_number.toString().padStart(3, '0') 
    new_tr.item(0).appendChild(save_input) 
}

function change_all(td_number, changed_tr){
    var new_value = changed_tr.value
    if (!isNaN(parseFloat(new_value)) && isFinite(new_value)){
        var table_size = document.querySelectorAll('tr')
        for(i = 1; i < table_size.length; i++){
            var all_tr = document.querySelectorAll('tr')[i].children
            all_tr.item(td_number).querySelector('input').value = new_value
        }
    }
    else{
        alert("Введено не число")
    }
}

function del_str(tr){
    if(table_counter != 1){
        tr.closest('tr').remove()
        table_counter -= 1
    }
}