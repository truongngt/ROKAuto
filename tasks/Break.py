import traceback

from tasks.Task import Task
from tasks.constants import TaskName
from random import randrange

import time


class Break(Task):
    def __init__(self, bot):
        super().__init__(bot)

    def do(self, next_task = TaskName.COLLECTING):
        irand = randrange(30, self.bot.config.breakTime)
        try:
            super().set_text(title='Break', remove=True)
            super().set_text(insert='Init View')
            super().call_idle_back()
            super().heal_troops()
            super().set_text(insert='0/{} seconds'.format(irand))
            super().back_to_home_gui()
            super().home_gui_full_view()

            # stop game if config set true
            if self.bot.config.terminate:
                super().stopRok()

            count = 0
            for i in range(irand):
                time.sleep(1)
                count = count + 1
                super().set_text(replace='{}/{} seconds'.format(count, irand), index=0)
            return next_task
        except Exception as e:
            traceback.print_exc()
            return next_task

    def do_no_wait(self, next_task = TaskName.COLLECTING):
        try:
            super().call_idle_back()
            super().heal_troops()
            return next_task
        except Exception as e:
            traceback.print_exc()
            return next_task
