# Learning Plotly

## Layouts

The `app.layout` module describes aesthetics and a hierarchical tree of components

* dash_html_components library contains a comoponent for every html tag
* not all components are pure html. Some are React hybrids
* Dash is declarative: you will primarily describe your application through these attributes
* CSS can be loaded like so:
```python
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
```

* HTML strings can be written in Markdown

### Examples

#### Declaring a text control

```python
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])
```

* dash.dependencies - needed for the callbacks, but dcc is the package doing the work
* html.Div passes an array of declarative statements that will render controls

### 



## Callbacks

Callbacks provide the means for the user to interact with the application

```python
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)
```

* `@app.callback` decorator describes application interface, wiring input and output sources
* `component_property='children'` Note that a value for 'children' is not defined in the Layout declaration. Dash will populate this when rendering the initial state (called _reactive programming_)
* If possible, expensive initialization (like downloading or querying data) should be done in the global scope of the app instead of within the callback functions.
* callbacks should **never mutate variables outside of their scope**. If your callbacks modify global state, then one user's session might affect the next user's session and when the app is deployed on multiple processes or threads, those modifications will not be shared across sessions
* Even though only a single Input changes at a time (a user can only change the value of a single Dropdown in a given moment), **Dash collects the current state of all of the specified Input properties and passes them into your function** for you



## Core Components worth investigating

* **Interactive Tables**: Dash is currently incubating an interactive table component that provides built-in filtering, row-selection, editing, and sorting. Prototypes of this component are being developed in the [`dash-table-experiments`](https://github.com/plotly/dash-table-experiments)
* **Upload component**: provides means to upload own data files for analysis: [examples](https://dash.plot.ly/dash-core-components/upload)
* **Graph component**: the core visualization package, shares the same syntax as the Plotly.py library. Fundamental docs and examples provided at [`Plotly Documentation`](https://plot.ly/python/)
* **Gauge**: Just fucking cool looking way to represent a single dimension of data



## Ideas

* Temporal
  * Content creation over time
  * Life journey of a document