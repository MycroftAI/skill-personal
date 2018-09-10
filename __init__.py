# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mycroft.skills.core import MycroftSkill, intent_file_handler


class PersonalSkill(MycroftSkill):

    def __init__(self):
        super(PersonalSkill, self).__init__(name="PersonalSkill")

    @intent_file_handler("WhenWereYouBorn.intent")
    def handle_when_were_you_born_intent(self, message):
        self.speak_dialog("when.was.i.born")

    @intent_file_handler("WhereWereYouBorn.intent")
    def handle_where_were_you_born_intent(self, message):
        self.speak_dialog("where.was.i.born")

    @intent_file_handler("WhoMadeYou.intent")
    def handle_who_made_you_intent(self, message):
        self.speak_dialog("who.made.me")

    @intent_file_handler("WhoAreYou.intent")
    def handle_who_are_you_intent(self, message):
        name = self.config_core.get("listener", {}).get("wake_word",
                                                        "mycroft")
        name = name.lower().replace("hey ", "")
        self.speak_dialog("who.am.i", {"name": name})

    @intent_file_handler("WhatAreYou.intent")
    def handle_what_are_you_intent(self, message):
        self.speak_dialog("what.am.i")

    @intent_file_handler("DoYouRhyme.intent")
    def handle_do_you_rhyme(self, message):
        self.speak_dialog("tell.a.rhyme")


def create_skill():
    return PersonalSkill()
