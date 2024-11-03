(function($) {
  "use strict"; // Start of use strict

  // Toggle the side navigation
  $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
    if ($(".sidebar").hasClass("toggled")) {
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Close any open menu accordions when window is resized below 768px
  $(window).resize(function() {
    if ($(window).width() < 768) {
      $('.sidebar .collapse').collapse('hide');
    };
    
    // Toggle the side navigation when window is resized below 480px
    if ($(window).width() < 480 && !$(".sidebar").hasClass("toggled")) {
      $("body").addClass("sidebar-toggled");
      $(".sidebar").addClass("toggled");
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
    if ($(window).width() > 768) {
      var e0 = e.originalEvent,
        delta = e0.wheelDelta || -e0.detail;
      this.scrollTop += (delta < 0 ? 1 : -1) * 30;
      e.preventDefault();
    }
  });

  // Scroll to top button appear
  $(document).on('scroll', function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(e) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    e.preventDefault();
  });

  
  // Evento del botón "Generar Reporte"
  $('#generarReporteBtn').on('click', function () {
    $(this).prop('disabled', true);
    $(this).text('Generando reporte...');

    // Enviar el formulario vía AJAX
    var formData = new FormData($('#formularioNuevoReporte')[0]); // Reemplaza 'actividadForm' con el ID de tu formulario
    $.ajax({
        url: '/nuevo_reporte/', // Reemplaza con la URL correcta de tu vista
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
          if (data.status === 'listo') {
            window.location.href = data.redirect_url;
        } else {
            // Aquí puedes agregar un mensaje al usuario indicando que el reporte aún se está generando
            console.log("El reporte aún no está listo.");
        }
        },
        error: function() {
          console.error("Error al generar el reporte.");
        },
        complete: function() {
            // Verificar estado del reporte (polling)
            checkReportStatus();
        }
    });
});

// Función para verificar el estado del reporte (polling)
function checkReportStatus() {
    $.ajax({
        url: '/nuevo_reporte/', // Reemplaza con la URL correcta de tu vista
        type: 'GET',
        success: function(data) {
            if (data.status === 'listo') {
                window.location.href = data.redirect_url;
            } else {
                setTimeout(checkReportStatus, 1000); // Verificar cada segundo
            }
        }
    });
}
})(jQuery); // End of use strict