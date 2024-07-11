document.addEventListener('DOMContentLoaded', function() {
  const startInput = document.getElementById('start');
  const endInput = document.getElementById('end');
  const saveButton = document.getElementById('save');

  chrome.storage.sync.get(['blockStart', 'blockEnd'], function(data) {
    startInput.value = data.blockStart || "09:00";
    endInput.value = data.blockEnd || "17:00";
  });

  saveButton.addEventListener('click', function() {
    const blockStart = startInput.value;
    const blockEnd = endInput.value;

    chrome.storage.sync.set({ blockStart, blockEnd }, function() {
      alert('Blocking times saved!');
    });
  });
});
