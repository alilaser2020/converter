import PySimpleGUI as sg

sg.theme("Dark")

layout = [
    [sg.Input(key="-INPUT-"),
     sg.Spin(["km to m", "m to cm", "min to sec", "Gb to Kb"], key="-SPIN-"),
     sg.Button("Enter", key="-ENTER-")],
    [sg.Text("Output", key="-OUTPUT-")],
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-ENTER-":
        if values["-SPIN-"] == "km to m":
            input_value = values["-INPUT-"]
            output_value = f"{input_value}km equal to {round(float(input_value) * 1000, 2)}m"
        if values["-SPIN-"] == "m to cm":
            input_value = values["-INPUT-"]
            output_value = f"{input_value} equal to {round(float(input_value) * 100, 2)}cm"
        if values["-SPIN-"] == "min to sec":
            input_value = values["-INPUT-"]
            output_value = f"{input_value}min equal to {round(float(input_value) * 60, 2)}sec"
        if values["-SPIN-"] == "Gb to Kb":
            input_value = values["-INPUT-"]
            output_value = f"{input_value}Gb equal to {int(input_value) * 1024}Kb"
        window["-OUTPUT-"].update(output_value)
window.close()
