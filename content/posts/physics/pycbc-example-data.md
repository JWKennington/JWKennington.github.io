Title: Loading Gravitational Wave Data with PyCBC
Date: 2019-10-12
Category: Physics
Tags: physics, gravity

This post is the first in a series of in-depth examples for analyzing gravitatonal wave data in Python, 
using the PyCBC package. There is also a notebook-version of this post, available [here](https://github.com/JWKennington/pycbc-examples),
in a repo of PyCBC examples.

## Motivation
In order to analyze observed gravitational waves, we must first find the data containing the signal. This 
example shows how to explore the Catalog of observed mergers available via the Gravitational Wave Open 
Science Center (GWOSC). Though this example focuses on the Python API, the list of available mergers can also 
be found on the web at the following [url](https://www.gw-openscience.org/catalog/GWTC-1-confident/html/).

<p style="background: #e6e6e6; border-radius: 10px; padding: 10px">
    <i><b>Developer Note:</b></i><br>
    The below example also uses the <a href="https://github.com/JWKennington/gravtools">gravtools</a> package, which 
    is just a small collection of convenience functions and utilities.
</p>

    :::python
    >>> from pycbc import catalog, frame
    >>> from gravtools import MergerParameters, Observatory, merger, time
<br>

## Exploring the Catalog
A common structure for grouping astonomical data, a Catalog is a sensible concept for a programmatic API. 
The PyCBC package has taken this approach, which is shown below using the `Catalog` class.

### The `Catalog` Class
The PyCBC Catalog class is capable of using the GWOSC data api to see essentially the same information
contained in the link above (albeit through JSON instead of HTML). Under the hood, PyCBC relies on AstroPy
data-access file-download utilities.

We can create a catalog simply by creating an instance of the `Catalog` class, and specifying a data source. 
In this case we specify `'gwtc-1'` which refers to the Gravitational-Wave Transient Catalog 1. This catalog 
consists of compact binary mergers observed in the O1 and O2 runs, and is also the default catalog (so you don't 
need to specify it, though we do for clarity).

    :::python
    >>> cat = catalog.Catalog(source='gwtc-1')
<br>

### Where are the `Merger`s stored?
The Catalog class is an iterable with respect to the names of the mergers in the catalog, so you can pick your favorite 
technique to iterate over the available merger names (we use the list coercion function below).

    :::python
    >>> # Get names of mergers in catalog 
    >>> merger_names = list(cat)  # Catalog class is iterable, any collection coercion will suffice
    >>> merger_names[:3]
    ['GW150914', 'GW151012', 'GW151226']
<br>

The Merger data associated to the name is stored in the `mergers` attribute of the `Catalog` instance, which 
is a dictionary keyed by the name of the merger (which we examined above). 

### Basic Merger Properties
The `Merger` object retrieved from the Catalog contains all the estimated parameters of the waveform. Each 
attribute may be accessed directly, but the preferred way is through the "median1d" method of the Merger class. 
Keep in mind that these parameters are in the *source* frame, not the *detector* frame.

<p style="background: #e6e6e6; border-radius: 10px; padding: 10px">
    <i><b>Developer Note:</b></i><br>
    Unfortunately, the merger-parameter attributes of the Merger instance are not inspectable in a code 
    editor due the way they are set during instantiation (using the setattr function). The 
    <i>gravtools.MergerParameters</i> enumeration contains all the relevant parameter names, 
    and _is_ inspectable, so we use it below.
</p>

    :::python
    >>> m = cat.mergers['GW150914']


    >>> # convenient summary string from gravtools
    >>> merger.summary(m)
    'Merger[GW150914](Mass1=35.6, Mass2=30.6, FinalSpin=0.69)'


    >>> # Log the names of the mergers in the catalog
    >>> print('Mergers in catalog:')
    >>> for name in merger_names:
            m = cat.mergers[name] # load the Merger object by name
            # the step above can also be done by instantiating a Merger object directly, e.g. catalog.Merger('GW150914')

            # Print some merger info by accessing parameters through the "median1d" method
            print('    {}: M1={:2.0f} M2={:2.0f} z={:2.2f}'.format(name,
                                                                m.median1d(MergerParameters.Mass1),     # m.mass1
                                                                m.median1d(MergerParameters.Mass2),     # m.mass2
                                                                m.median1d(MergerParameters.Redshift))) # m.redshift
    Mergers in catalog:
        GW150914: M1=36 M2=31 z=0.09
        GW151012: M1=23 M2=14 z=0.21
        GW151226: M1=14 M2= 8 z=0.09
        GW170104: M1=31 M2=20 z=0.19
        GW170608: M1=11 M2= 8 z=0.07
        GW170729: M1=51 M2=34 z=0.48
        GW170809: M1=35 M2=24 z=0.20
        GW170814: M1=31 M2=25 z=0.12
        GW170817: M1= 1 M2= 1 z=0.01
        GW170818: M1=36 M2=27 z=0.20
        GW170823: M1=40 M2=29 z=0.34
<br>

## Merger Strain
Though a Merger object loads several scalar parameters once instantiated, it does not automatically load the 
timeseries of strain data (for efficiency of the API). It is possible, however, and quite easy to load the 
strain timeseries around the event. The below code shows how to load the waveform data. We begin by choosing a 
specific merger from the catalog.

    :::python
    >>> # Pick a merger from the catalog
    >>> m = cat.mergers['GW170823']
<br>

### The `TimeSeries` Class
The time series data containing the merger waveform is returned as an instance of the `TimeSeries` class. Below, 
we show how to load the strain data, as well as how to do some useful manipulations.

<p style="background: #e6e6e6; border-radius: 10px; padding: 10px">
    <i><b>Developer Note:</b></i><br>
    The <i>pycbc.TimeSeries</i> class, which contains the merger strain data (as mentioned above), is a thin wrapper 
    around a numpy or pycuda array supporting many of the common array interface features, such as slicing. There is 
    also additional metadata, including the GPS starting and ending time of the waveform, as well as the time 
    interval between adjacent values in the array.
</p>

    :::python
    # Query the strain timeseries for the merger
    >>> ts = m.strain(ifo=Observatory.LIGOHanford) # the "ifo" argument refers to the observatory that recorded the strain

    >>> # Print the boundaries of the timeseries
    >>> print('Duration={:.0f}s Interval={:.1e}s Start={} End={}'.format(ts.duration, ts.delta_t, 
                                                                     time.gps_to_datetime(ts.start_time), 
                                                                     time.gps_to_datetime(ts.end_time)))

    >>> # Print the size of the underlying array
    >>> print('Array Size: {:,d}'.format(len(ts)))
    >>> # Supports Slicing
    >>> print('Array Size: {:,d}'.format(len(ts[:100])))

    Duration=32s Interval=2.4e-04s Start=2017-08-23 13:14:20 End=2017-08-23 13:14:52
    Array Size: 131,072
    Array Size: 100
<br>

<p style="background: #cce6ff; border-radius: 10px; padding: 10px">
    <i><b>Physics Note:</b></i><br>
    The <i>strain</i> recorded in the above timeseries basically represents the degree to which space has expanded 
    or contracted along the path of the interferometer:
    $h = \frac{\Delta L}{L},\quad \Delta L = L_x - L_y$
    Where $L$ is the original length of the detector, and the change is measured as the difference in the detector arms. For more information on the experimental setup, see the excellent review, <a href="https://link.springer.com/article/10.1007/s41114-016-0002-8">Interferometer techniques for gravitational wave detection</a> by Bond, Brown, Freise and Strain.
</p>

### Visualize the Time-Domain
This section is devoted to visualizing the Time-domain strain. We use the `sample_times` attribute of 
the `TimeSeries` class for the x-coordinates of the plot, and simply pass the `TimeSeries` object itself 
as the y-coordinates (since it is an array). 

    :::python
    # Import some plotting tools from the bokeh package
    from bokeh.plotting import output_notebook, show, figure
    output_notebook(hide_banner=True) # for Jupyter usage, otherwise it will write out files

    # Create the figure
    f = figure(title='Time-Domain data around ' + m.data['files']['eventName'], 
               x_axis_type='datetime', x_axis_label='Time (s)', y_axis_label='Strain',
               plot_height=300, plot_width=800)

    # Plot the line-plot data
    f.line(x=ts.sample_times.numpy(), y=ts.numpy())

    # Display
    show(f)


<br>
<p style="background: #e6e6e6; border-radius: 10px; padding: 10px">
    <i><b>Developer Note:</b></i><br>
    Plotting in Python is notoriously subjective; there are many competing libraries that all deserve proper attention, such as plotly, bokeh, plotnine, altair, and others (excluding matplotlib). There are meta-plotting libraries as well that sit atop these, such as holoviews. However, we choose to use Bokeh here primarily due to the simple interface, and clean style.
</p>


## Acknowledgments
This post is based on the official [PyCBC tutorials](https://pycbc.org/tutorials/), and is cited in the example 
repository's [README](https://github.com/JWKennington/pycbc-examples/blob/master/README.md). 
