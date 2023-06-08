      // Get references to the menu items
      var dashboardLi = document.querySelector('.dashboard');
      var registerLi = document.querySelector('.vehicle_register');
      // var settingsLi = document.querySelector('.settings');
      var updateLi = document.querySelector('.settings .update-profile');
      var deleteLi = document.querySelector('.settings .delete-profile');

      var helpLi = document.querySelector('.help');
      var signOutLi = document.querySelector('.sign_out');

      // Get references to the main content sections
      var dashboardContent = document.getElementById('dashboard-content');
      var registerContent = document.getElementById('register-content');
      var updateContent = document.querySelector('#settings-content .update');
      var deleteContent = document.querySelector('#settings-content .delete');
      var helpContent = document.getElementById('help-content');


      // Add event listeners to menu items
      dashboardLi.addEventListener('click', function() {
        hideAllContent();
        dashboardContent.classList.remove('hidden');
      });

      registerLi.addEventListener('click', function() {
        hideAllContent();
        registerContent.classList.remove('hidden');
      });

      updateLi.addEventListener('click', function() {
        hideAllContent();
        updateContent.classList.remove('hidden');
      });

      deleteLi.addEventListener('click', function() {
        hideAllContent();
        deleteContent.classList.remove('hidden');
      });

      helpLi.addEventListener('click', function() {
        hideAllContent();
        helpContent.classList.remove('hidden');
      });


      // Helper function to hide all content sections
      function hideAllContent() {
        dashboardContent.classList.add('hidden');
        registerContent.classList.add('hidden');
        updateContent.classList.add('hidden');
        deleteContent.classList.add('hidden');
        helpContent.classList.add('hidden');
      }

      // Show the default content initially
      hideAllContent();
      dashboardContent.classList.remove('hidden');
