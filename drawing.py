from fsm import TocMachine

machine = TocMachine(
    states=["user", "state1", "state2", "state3", "state4", "state5", "state6", "state7", "state8", "state9", "state10", "state11", "state12", "state13", "state14", "state15"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state3",
            "conditions": "is_going_to_state3",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state4",
            "conditions": "is_going_to_state4",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state5",
            "conditions": "is_going_to_state5",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state6",
            "conditions": "is_going_to_state6",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state7",
            "conditions": "is_going_to_state7",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state8",
            "conditions": "is_going_to_state8",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state9",
            "conditions": "is_going_to_state9",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state10",
            "conditions": "is_going_to_state10",
        },
    {
            "trigger": "advance",
            "source": "user",
            "dest": "state11",
            "conditions": "is_going_to_state11",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state12",
            "conditions": "is_going_to_state12",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state13",
            "conditions": "is_going_to_state13",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state14",
            "conditions": "is_going_to_state14",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state15",
            "conditions": "is_going_to_state15",
        },
        {"trigger": "go_back", "source": ["state1", "state2", "state3", "state4", "state5", "state6", "state7", "state8", "state9", "state10", "state11", "state12", "state13", "state14", "state15"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

machine.get_graph().draw("fsm.png", prog="dot", format="png")
