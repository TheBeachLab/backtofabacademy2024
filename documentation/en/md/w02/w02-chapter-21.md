## Wing Profile Simulation
[*under development*]{.mark .yellow}

I fly on an *ICP Savannah S* airplane with a modified NACA-65018[^211] wing profile. It's not very fast, but it can take off and land on very short distances and fly at very low speeds without stalling[^212]. Near the leading edge of the wing, there are some plastic parts called vortex generators. Their role is to create micro-turbulences to prevent the boundary layer from detaching from the wing. The goal in OpenFOAM is to simulate a section of the wing with and without vortex generators and verify the difference.

![](../../img/w02/avion.webp)

[^212]: A condition that occurs when the wing loses lift by exceeding the critical angle of attack.

[^211]: The numbers are parameters that can be input into equations to generate the cross-sectional shape and calculate its properties.

