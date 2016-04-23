(function () {

'use strict';

angular.module('OpenSlidesApp.openslides_csv_export.site', ['OpenSlidesApp.openslides_csv_export'])

.config([
    'mainMenuProvider',
    'gettext',
    function (mainMenuProvider, gettext) {
        mainMenuProvider.register({
            'ui_sref': 'csv_export_list_of_speakers',
            'img_class': 'download',
            'title': gettext('CSV Export'),
            'weight': 2000,
            'perm': 'agenda.can_manage',
        });
    }
]);

}());
