(function($) {
  $(function() {
      const $pageSectionsGroup = $('#pagesection_set-group');

      const toggleFields = ($sectionType) => {
        const $fieldset = $sectionType.parent().parent().parent();
        const $fields = $fieldset.find('.form-row:not(.field-section_type)');
        const $textItems = $fieldset.siblings('.djn-group[id*=textitem_set-group]').not('.djn-group[id*=icontextitem_set-group]');
        const $partners = $fieldset.siblings('.djn-group[id*=partner_set-group]');
        const $questions = $fieldset.siblings('.djn-group[id*=question_set-group]');
        const $iconTextItems = $fieldset.siblings('.djn-group[id*=icontextitem_set-group]');

        const show = (name) => {
          const $field = $fields.filter(`[class*=field-${name}]`);
          $field.show();
        };

        $textItems.hide();
        $iconTextItems.hide();
        $fields.hide();
        $partners.hide();
        $questions.hide();

        const value = $sectionType.val();

        console.log($fields);

        if (value === 'text') {
          show('title');
          show('text');
        } else if (value === 'text_image') {
          show('title');
          show('text');
          show('image_on_the_left');
          show('image');
        } else if (value === 'donate_cta') {
          show('cta');
        } else if (value === 'text_list') {
          $textItems.show();
        } else if (value === 'partners') {
          $partners.show();
        } else if (value === 'qa') {
          $questions.show();
        } else if (value === 'icon_text_list') {
          $iconTextItems.show();
        }
      };

      $pageSectionsGroup.find('.field-section_type select').each(function () {
        const $sectionType = $(this);
        toggleFields($sectionType);
      });

      $pageSectionsGroup.on('change', '.field-section_type select', function () {
        const $sectionType = $(this);
        toggleFields($sectionType);
      });

      window.$ = $;
  });
})(jQuery);