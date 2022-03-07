import traceback

from tasks.Task import Task
from tasks.constants import BuildingNames
from filepath.file_relative_paths import ImagePathAndProps


from tasks.constants import TaskName


class Build(Task):
    def __init__(self, bot):
        super().__init__(bot)

    def do(self, next_task=TaskName.BUILD):
        try:
            upgrade_green_point = (640, 444)
            upgrade_confirm_point = (992, 551)
            first_build_point = (255, 500)
            super().set_text(title='Build', remove=True)
            super().back_to_home_gui()
            super().home_gui_full_view()

            # tap on builder's hunter
            super().set_text(insert='Open City Hall')
            x, y = self.bot.building_pos[BuildingNames.CITY_HALL.value]
            super().tap(x, y, 3)

            _, _, city_hall_btn_pos = self.gui.check_any(
                ImagePathAndProps.CITY_HALL_BTN_IMAGE_PATH.value)
            if city_hall_btn_pos is None:
                return
            x, y = city_hall_btn_pos
            x = x - 65
            super().set_text(insert='Tap upgrade button at ({}, {})'.format(x, y))
            super().tap(x, y, 2)

            _, _, go_btn_pos = self.gui.check_any(
                ImagePathAndProps.GO_BTN_IMAGE_PATH.value)
            if go_btn_pos is None:
                x, y = upgrade_confirm_point
                super().set_text(insert='Tap upgrade confirm button at ({}, {})'.format(x, y))
                super().tap(x, y, 1)
            else:
                x, y = go_btn_pos
                super().set_text(insert='Tap go button at ({}, {})'.format(x, y))
                super().tap(x, y, 2)

                continue_flag = True
                while (continue_flag) :
                    _, _, upgrade_btn_pos = self.gui.check_any(ImagePathAndProps.UPGRADE_BTN_IMAGE_PATH.value)
                    if upgrade_btn_pos is None:
                        continue_flag = False
                    
                    x, y = upgrade_btn_pos
                    super().set_text(insert='Tap upgrade button at ({}, {})'.format(x, y))
                    super().tap(x, y, 2)

                    _, _, go_btn_pos = self.gui.check_any(
                        ImagePathAndProps.GO_BTN_IMAGE_PATH.value)
                    if go_btn_pos is None:
                        x, y = upgrade_confirm_point
                        super().set_text(insert='Tap upgrade confirm button at ({}, {})'.format(x, y))
                        super().tap(x, y, 1)
                        continue_flag = False
                    else:
                        x, y = go_btn_pos
                        super().set_text(insert='Tap go button at ({}, {})'.format(x, y))
                        super().tap(x, y, 2)

        except Exception as e:
            traceback.print_exc()
            return next_task
        return next_task