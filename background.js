const blockedWebsites = ["*://www.facebook.com/*", "*://www.twitter.com/*"];

chrome.storage.sync.get(["blockStart", "blockEnd"], (data) => {
  const blockStart = data.blockStart || "09:00";
  const blockEnd = data.blockEnd || "17:00";

  chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
      const currentTime = new Date();
      const startTime = new Date();
      const endTime = new Date();

      const [startHour, startMinute] = blockStart.split(":");
      const [endHour, endMinute] = blockEnd.split(":");

      startTime.setHours(startHour, startMinute, 0);
      endTime.setHours(endHour, endMinute, 0);

      if (currentTime >= startTime && currentTime <= endTime) {
        return { cancel: true };
      }
    },
    { urls: blockedWebsites },
    ["blocking"]
  );
});

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ blockStart: "09:00", blockEnd: "17:00" });
});
