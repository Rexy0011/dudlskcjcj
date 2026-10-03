
(function() {
  const nopecha_api_key = 'ipkbdpx3n5mjv5mlf2354wb37u7nrnad';
  chrome.storage.local.set({'nopecha_key': nopecha_api_key}, function() {
    console.log('[NopeCHA Storage] API Key initialized');
  });
})();
