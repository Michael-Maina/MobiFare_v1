      // Get references to the menu items
      var dashboardLi = document.querySelector('.dashboard');
      var paymentLi = document.querySelector('.payment');
      var settingsLi = document.querySelector('.settings');
      var helpLi = document.querySelector('.help');
      var signOutLi = document.querySelector('.sign_out');

      // Get references to the main content sections
      var dashboardContent = document.getElementById('dashboard-content');
      var settingsContent = document.getElementById('settings-content');
      var helpContent = document.getElementById('help-content');
      var paymentContent = document.getElementById('payment-content');



      // Add event listeners to menu items
      dashboardLi.addEventListener('click', function() {
        hideAllContent();
        dashboardContent.classList.remove('hidden');
      });

      settingsLi.addEventListener('click', function() {
        hideAllContent();
        settingsContent.classList.remove('hidden');
      });

      paymentLi.addEventListener('click', function() {
        hideAllContent();
        paymentContent.classList.remove('hidden');
      });

      helpLi.addEventListener('click', function() {
        hideAllContent();
        helpContent.classList.remove('hidden');
      });


      // Helper function to hide all content sections
      function hideAllContent() {
        dashboardContent.classList.add('hidden');
        settingsContent.classList.add('hidden');
        helpContent.classList.add('hidden');
        paymentContent.classList.add('hidden');
      }

      // Show the default content initially
      hideAllContent();
      dashboardContent.classList.remove('hidden');
