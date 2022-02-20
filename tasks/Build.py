from tasks.Task import Task
from tasks.constants import BuildingNames
from filepath.file_relative_paths import ImagePathAndProps


from tasks.constants import TaskName


class Build(Task):
    def __init__(self, bot):
        super().__init__(bot)

    def do(self, next_task=TaskName.BUILD):
        upgrade_green_point = (640, 444)
        upgrade_confirm_point = (992, 551)
        first_build_point = (255, 500)
        super().set_text(title='Build', remove=True)
        
        for x in range(2):
            super().back_to_home_gui()
            super().home_gui_full_view()
            
            # tap on builder's hunter
            super().set_text(insert='Open Builder''s Hunter')
            x, y = self.bot.building_pos[BuildingNames.BUILDERS_HUT.value]
            super().tap(x, y, 3)

            # find and tap on build icon
            super().set_text(insert='Open Builder Management')
            _, _, build_icon_btn_pos = self.gui.check_any(ImagePathAndProps.BUILD_ICON_BTN_IMAGE_PATH.value)
            if build_icon_btn_pos is None:
                continue
            x, y = build_icon_btn_pos
            super().tap(x, y, 3)

            # find and tap on build button
            super().set_text(insert='Click BUILD button')
            _, _, build_btn_pos = self.gui.check_any(ImagePathAndProps.BUILD_BTN_IMAGE_PATH.value)
            if build_btn_pos is None:
                continue
            x, y = build_btn_pos
            super().tap(x, y, 3)

            # find new build
            super().set_text(insert='New build')
            _, _, city_editor_btn_pos = self.gui.check_any(ImagePathAndProps.CITY_EDITOR_BTN_IMAGE_PATH.value)
            if city_editor_btn_pos is None:
                # tap on upgrade green button
                x, y = upgrade_green_point
                super().tap(x, y, 3)

                # tap on confirm button
                x, y = upgrade_confirm_point
                super().tap(x, y, 3)
            else:
                # click to first
                x, y = first_build_point
                super().tap(x, y, 3)

                _, _, tick_btn_pos = self.gui.check_any(ImagePathAndProps.TICK_BTN_IMAGE_PATH.value)
                if tick_btn_pos is None:
                    continue
                x, y = tick_btn_pos
                super().tap(x, y, 3)
        else:
            next_task
