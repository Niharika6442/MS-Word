// taskpane.js
Office.onReady(function (info) {
   if (info.host === Office.HostType.Word) {
       // Assign event handler to button click
       document.getElementById("summarizeButton").onclick = summarizeDocument;
   }
});
function summarizeDocument() {
   // Get document content
   Word.run(function (context) {
       var body = context.document.body;
       context.load(body, 'text');
       return context.sync().then(function () {
           // Call Python API to get summary
           fetch('http://your-python-api-url/summarize', {
               method: 'POST',
               headers: {
                   'Content-Type': 'application/json',
               },
               body: JSON.stringify({ document_content: body.text }),
           })
           .then(response => response.json())
           .then(data => {
               // Display the summary in the task pane
               document.getElementById('summaryResult').innerText = data.summary;
           })
           .catch(error => console.error('Error:', error));
       });
   });
}