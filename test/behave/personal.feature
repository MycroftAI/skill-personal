Feature: mycroft-personal

  Scenario: Poem contest
    Given an english speaking user
     When the user says "do you rhyme"
     Then "mycroft-personal" should reply with dialog from "tell.a.rhyme.dialog"

  Scenario: what are you
    Given an english speaking user
     When the user says "what are you"
     Then "mycroft-personal" should reply with dialog from "what.am.i.dialog"

  Scenario: when were you born
    Given an english speaking user
     When the user says "when were you born"
     Then "mycroft-personal" should reply with dialog from "when.was.i.born.dialog"

  Scenario: where were you born
    Given an english speaking user
     When the user says "where were you born"
     Then "mycroft-personal" should reply with dialog from "where.was.i.born.dialog"

  Scenario: who are you
    Given an english speaking user
     When the user says "who are you"
     Then "mycroft-personal" should reply with dialog from "who.am.i.dialog"

  Scenario: who made you
    Given an english speaking user
     When the user says "who made you"
     Then "mycroft-personal" should reply with dialog from "who.made.me.dialog"
