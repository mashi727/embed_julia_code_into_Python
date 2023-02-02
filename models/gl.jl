function GLCalc()
    nx = 100
    ny = 51
    x = range(-10,stop=10,length=nx)
    y = range(-10,stop=10,length=ny)

    z = zeros(Float64, length(x), length(y))

    for iy = 1:length(y)
        for ix = 1:length(x)
            d = (x[ix]^2 + y[iy]^2)^0.5
            z[ix, iy] = 10 * cos(d) / (d+1)
        end
    end
    return x,y,z
end

