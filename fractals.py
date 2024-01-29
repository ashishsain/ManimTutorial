from manim import *

class trinagle_fractal(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        frame=self.camera.frame
        tri=Triangle()
        for i in range(10):
            triangle = VGroup(*[tri.copy() for _ in range(3)])
            triangle[1].next_to(triangle[0], RIGHT)
            new_t = VGroup(triangle[0], triangle[1])
            triangle[2].next_to(new_t, UP)
            self.play(frame.animate.move_to(triangle.get_center()).set_height(triangle.get_height()*1.5))
            self.play(Create(triangle))
            self.wait(1)
            tri=triangle

class pytha_gorean_fractal(MovingCameraScene):
    def construct(self):
        group=VGroup()

        def draw_square(corner,base_v, angle, length):
            sqaure = VMobject()
            height=np.array([-base_v[1], base_v[0], 0])
            point=[corner, corner + base_v, corner + base_v + height, corner + height, corner]
            sqaure.set_points_as_corners(point)
            group.add(sqaure.set_fill(np.random.choice([RED,GREEN,YELLOW,PINK]),opacity=1))
            if length>0:
                corner1=corner+height
                width=np.sqrt(norm_squared(base_v))
                base1_v_h=width*np.cos(angle)*np.cos(angle)
                base1_v_v=width*np.cos(angle)*np.sin(angle)
                base1_v=normalize(base_v)*base1_v_h+normalize(height)*base1_v_v
                draw_square(corner1,base1_v,angle,length-0.2)

                #drawing right sqaure
                beta=90*DEGREES-angle
                corner2 = corner1 + base1_v
                width = np.sqrt(norm_squared(base_v))
                base2_v_h = width * np.sin(angle) * np.cos(beta)
                base2_v_v = width * np.sin(angle) * np.sin(beta)
                base2_v = normalize(base_v) * base2_v_h - normalize(height) * base2_v_v
                draw_square(corner2, base2_v, angle, length - 0.2)
            return group
        squares=draw_square(3*DOWN,RIGHT,0*DEGREES,1)
        an=MathTex("Angle=0^{\\circ}").to_corner(LEFT+UP)
        self.add(squares,an)
        for ang in np.insert(np.arange(0,90, 10)[1:],4,45):
            group = VGroup()
            squares1 = draw_square(3*DOWN, RIGHT, ang*DEGREES, 1)
            ang1 = MathTex("Angle=",str(ang),"^{\\circ}").to_corner(LEFT + UP)
            self.play(Transform(squares, squares1),Transform(an,ang1))
        self.wait()


# call the function of which you want to create ftactals
class recursion_fractals(MovingCameraScene):
    def construct(self):
        # this camera configuration for binary tree

        # self.camera.frame.save_state()
        # self.camera.frame.scale(3)
        # self.camera.frame.shift(10*UP)

        ##########################################circle fractals##################################
        circles = VGroup()

        def circle(radius, x, y):
            cir = Circle(radius=radius / 2, color=YELLOW).move_to(np.array([x, y, 0]))
            circles.add(cir)
            if radius > 0.2:
                circle(radius / 2, x + radius / 2, y)
                circle(radius / 2, x - radius / 2, y)
            return circles

        ###############################end circle fractals#########################################

        #####################################counter fractals######################################
        couters = VGroup()

        def counter(sx, sy, ln):
            line = Line(np.array([sx, sy, 0]), np.array([sx + ln, sy, 0]), color=YELLOW)
            couters.add(line)
            if ln > 0.1:
                sy -= 0.5
                counter(sx, sy, ln / 3)
                counter(sx + ln * 2 / 3, sy, ln / 3)
            return couters

        coun = counter(-config.frame_width / 2, 0, config.frame_width)
        self.play(AnimationGroup(*[Create(t) for t in coun], lag_ratio=0.4))
        #####################################end fractls#######################################

        #################################binary tree fractals##################################
        group = VGroup()

        def tree(length, angle, point, angle1):
            line = Line(ORIGIN, length * UP, color=GREEN)
            # self.play(line.animate.shift(point))
            # self.play(line.animate.rotate(angle, about_point=point))
            line.shift(point)
            line.rotate(angle, about_point=point)
            # self.play(Create(line))
            group.add(line)
            # self.add(line)
            if length > 0.1:
                tree(length / 1.5, angle + angle1 * DEGREES, line.get_end(), angle1)
                tree(length / 1.5, angle - angle1 * DEGREES, line.get_end(), angle1)
            return group

        # calling binary tree method is given below in commented code

        # binary tree
        # tr=tree(7,0,0,10)
        # ang = ArcBetweenPoints(tr[0].point_from_proportion(0.9), tr[1].point_from_proportion(0.1), angle=-TAU / 4)
        # label = MathTex("10^{\\circ}").next_to(ang, LEFT)
        # self.play(AnimationGroup(*[Create(t) for t in tr],lag_ratio=0.001))
        # self.play(Create(ang),Create(label))
        # self.wait(2)
        # for an in np.arange(0,90+10,10)[2:]:
        #     group=VGroup()
        #     tr1=tree(7,0,0,an)
        #     ang1 = ArcBetweenPoints(tr1[0].point_from_proportion(0.9), tr1[1].point_from_proportion(0.1), angle=-TAU / 4)
        #     label1 = MathTex(str(an),"^{\\circ}").next_to(ang, LEFT)
        #     self.play(Transform(tr,tr1),Transform(ang,ang1),Transform(label,label1))
        # self.wait(2)

        # given below commented code is dragon curve fractals code

        # line=Line(ORIGIN,RIGHT)
        # point=line.get_end()
        # self.add(line)
        # for i in range(10):
        #     c=VGroup(*[line.copy() for _ in range(2)])
        #     self.add(c[0].set_color(RED))
        #     c[1].set_color(YELLOW)
        #     self.play(c[1].animate.rotate(90*DEGREES,about_point=point))
        #
        #     line=c
        #     point=list(reversed(c[1].get_all_points()))[-1]
        #     self.camera.frame.set_height(c.get_height() * 2)
        #     self.camera.frame.move_to(c)



class Dragon(MovingCameraScene):
    def construct(self) -> None:
        line = Line(ORIGIN, RIGHT)
        point = line.get_end()
        self.add(line)
        for i in range(10):
            c = VGroup(*[line.copy() for _ in range(2)])
            self.add(c[0].set_color(RED))
            c[1].set_color(YELLOW)
            self.play(c[1].animate.rotate(90 * DEGREES, about_point=point))
            line = c
            point = list(reversed(c[1].get_all_points()))[-1]
            self.camera.frame.scale(1.3)
            self.camera.frame.move_to(c)
        self.wait(2)

