#include <pybind11/pybind11.h>

int new_add(int i, int j) {
    return i + j;
}

namespace py = pybind11;

PYBIND11_MODULE(new_example, mod) {
    mod.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: new_example

        .. autosummary::
           :toctree: _generate

           new_add
    )pbdoc";

    mod.def("new_add", &new_add, R"pbdoc(
        Add two numbers

        Some other explanation about the new_add function.
    )pbdoc");

#ifdef VERSION_INFO
    mod.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    mod.attr("__version__") = "dev";
#endif
}
