$(document).ready(function() {
    // Make a request using Ajax to fetch ice cream details
    $.ajax({
        url: '/menu-app/menu-data/',
        method: 'GET',
        success: function(response) {
            // Access the 'ice cream details' array from the response
            var iceCreamItems = response['ice_cream_details'];

            var tableBody = $('#ice-cream-table tbody');

            // Iterate through the ice cream items
            iceCreamItems.forEach(function(item) {
                // Create a new row for each item
                var row = $('<tr>')

                // Create table cells and populate data
                var cellName = $('<td>').text(item.ice_cream_name);
                var cellFlavour = $('<td>').text(item.ice_cream_flavour);
                var cellWeight = $('<td>').text(item.ice_cream_weight);

                // create a link for update
                var updateButton = $('<a href="/menu-app/update/' + item.ice_cream_id + '/">')
                    .text('Update')
                    .attr('data-id', item.id);

                // create a link for delete
                var deleteButton = $('<a href="#">')
                    .text('Delete')
                    .attr('data-id', item.id);

                var cellAction1 = $('<td>').append(updateButton);

                var cellAction2 = $('<td>').append(deleteButton);

                // Append the cells to the row
                row.append(cellName, cellFlavour, cellWeight,cellAction1,cellAction2);

                // Append the row to the table body
                tableBody.append(row);
                deleteButton.click(function(event){
                    event.preventDefault();
                    var confirmation = confirm('Do you want to delete this ice cream item?');


                    if (confirmation){
                        var csrfToken = $('meta[name="csrf-token"]').attr('content');
                        $.ajax({
                            url: '/menu-app/delete/' + item.ice_cream_id + '/',
                            method: 'DELETE',
                            headers: {
                                'X-CSRFToken': csrfToken
                            },
                            success: function(response){
                                row.remove();
                                alert('Ice Cream Item Deleted Successfully');
                            },
                            error: function(xhr,status,error){
                                console.error('Failed to delete item' + error);
                                alert("Error deleting item");
                            }
                        });
                    }
                });

            });
        },
        error: function(xhr, status, error) {
            console.error('AJAX request failed: ' + error);
        }
    });
});
