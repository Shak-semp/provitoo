function searchForPerson(){
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("person");
    filter = input.value.toUpperCase();
    table = document.getElementById("personList");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (!td) {
            continue;
        }
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
            continue;
        }
        td = tr[i].getElementsByTagName("td")[1];
        if (!td) {
            continue;
        }
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
            continue;
        }
        tr[i].style.display = "none";
    }
}
function searchForCompany(){
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("companyOrPerson");
    filter = input.value.toUpperCase();
    table = document.getElementById("companyList");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (!td) {
            continue;
        }
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
            continue;
        }
        td = tr[i].getElementsByTagName("td")[1];
        if (!td) {
            continue;
        }
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
            continue;
        }
        td = tr[i].getElementsByTagName("td")[2];
        if (!td) {
            continue;
        }
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
            continue;
        }
        tr[i].style.display = "none";
    }
}
/*
$(document).ready(function(){
    $("#companyOrPerson").on("input", function(e){
        $("#results").empty();
        $.ajax({
            method: "post",
            url: "/search",
            data: {searchText: $("#companyOrPerson").val()},
            success: function(res){
                console.log(res)
                console.log(JSON.stringify(res, null, 2))
                var data = "<div>"
                $.each(res, function(index, value){
                    data += "<p>" + value.name + "</p>"
                    data += "<p>" + value.regCode + "</p>"
                })
                data += "</div>"
                $("#results").html(data);
            }
        });
    });
});
*/
function checkIfEnable(buttonId){
    btnId =  buttonId + "button";
    inputId = "cut" + buttonId;
    input = document.getElementById(inputId);
    if(input.value > 0){
        document.getElementById(btnId).disabled = false;
    } else {
        document.getElementById(btnId).disabled = true;
    }
}
function addPerson(rowId){
    rowNumber = parseInt(rowId.id);
    rowTrueId = "rowId" + rowNumber;
    inputId = "cut" + rowNumber;
    temp = document.getElementById(rowTrueId);
    tempCut = document.getElementById(inputId).value;
    info = "Osa suurus: " + tempCut;
    capital = document.getElementById('capital').value;
    document.getElementById('capital').setAttribute("value", parseInt(document.getElementById('capital').value) + parseInt(tempCut));
    for(var a = 0; a < document.getElementById('personList').rows.length; a++){
        if(document.getElementById('personList').rows[a] != temp){
            continue;
        }
        document.getElementById("personList").deleteRow(a);
    }
    tempRow = "<tr id=outcome" + rowNumber + ">";
    $('#shareList').after("<tr>");
    for(var y = 0; y < 3; y++){
        tempRow = tempRow + "<td>" + temp.cells[y].innerHTML + "</td>";
    }
    tempRow = tempRow + "<td>" + info + "</td>" + "</tr>";
    $("#shareList").find('tbody').append(tempRow);
    if(document.getElementById('selectedPersonsId').value == ""){
        document.getElementById('selectedPersonsId').value = rowNumber;
    } else {
        document.getElementById('selectedPersonsId').value = document.getElementById('selectedPersonsId').value + ", " + rowNumber;
    }
    
    if(document.getElementById('shareInCompany').value == ""){
        document.getElementById('shareInCompany').value = tempCut
    } else {
        document.getElementById('shareInCompany').value = document.getElementById('shareInCompany').value + ", " + tempCut
    }
}
$('.submitButton').click(function() {
    $('#selectedCompany').val(parseInt(this.id));
})
$('.addMoney').click(function() {
    person = parseInt(this.id);
    cutId = "#cut" + person;
    temp = $('#addMoney').val();
    $('#addMoney').val(temp + person + "," + $(cutId).val());
    console.log($('#addMoney').val)
})